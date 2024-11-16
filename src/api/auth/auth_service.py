import jwt
from typing import Dict, Union, Literal, Callable, List
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer
from asyncpg import Record

# Local
from src.settings import api_settings
from src.api.enums_sett import APIRoutersData, AuthEnum
from src.db.repository.user_repository import UserRepository
from src.api.core.exceptions import AuthExcp


class AuthService:

    convert_auth: OAuth2PasswordBearer = OAuth2PasswordBearer(
        tokenUrl=APIRoutersData.API_V1_PREFIX.value
        + APIRoutersData.AUTH_PREFIX.value
        + "/login",
        description="Система аутентификации",
    )

    @classmethod
    def create_tokens(cls, user_id: int) -> Union[bool, Dict[str, str]]:
        try:
            data = {"sub": user_id}
            data.update(
                {
                    "exp": datetime.utcnow()
                    + timedelta(minutes=api_settings.TIME_TOKEN_WORK)
                }
            )
            access_token = jwt.encode(
                data, api_settings.JWT_SECRET_KEY, algorithm=api_settings.ALG
            )
            data["exp"] = datetime.utcnow() + timedelta(
                days=api_settings.TIME_REFRESH_WORK
            )
            refresh_token = jwt.encode(
                data, api_settings.JWT_REFRESH_SECRET_KEY, algorithm=api_settings.ALG
            )
            return {"Access-Token": access_token, "Refresh-Token": refresh_token}
        except jwt.PyJWTError:
            return False

    @classmethod
    def decode_tokens(
        cls, type_token: Literal["access", "refresh"], token
    ) -> Union[Dict[str, Union[str, int]], bool]:
        try:
            match type_token:
                case AuthEnum.ACCESS.value:
                    return jwt.decode(
                        jwt=token,
                        key=api_settings.JWT_SECRET_KEY,
                        algorithms=api_settings.ALG,
                        options={"verify_exp": True},
                    )
                case AuthEnum.REFRESH.value:
                    return jwt.decode(
                        jwt=token,
                        key=api_settings.JWT_REFRESH_SECRET_KEY,
                        algorithms=api_settings.ALG,
                        options={"verify_exp": True},
                    )
                case "_":
                    return False
        except jwt.DecodeError:
            return False
        except jwt.ExpiredSignatureError:
            return False

    @classmethod
    def update_access_token(cls, refresh_token) -> Dict[str, str]:
        try:
            token_decode: Dict[str, str] = cls.decode_tokens(
                type_token="refresh", token=refresh_token
            )

            token_decode.update(
                {
                    "exp": datetime.utcnow()
                    + timedelta(minutes=api_settings.TIME_TOKEN_WORK)
                }
            )
            new_access_token = jwt.encode(
                payload=token_decode,
                key=api_settings.JWT_SECRET_KEY,
                algorithm=api_settings.ALG,
            )

            return {"Access-Token": new_access_token}
        except jwt.DecodeError:
            return False
        except jwt.ExpiredSignatureError:
            return False

    def __call__(self, type_token: str, hash=None):
        def func_wrapper(func: Callable):
            async def wrapper(*args, **kwargs) -> str:
                match type_token:
                    case AuthEnum.DECODE.value:
                        user_data = self.decode_tokens(
                            type_token="access", token=kwargs["token"]
                        )
                        if not user_data:
                            await AuthExcp.no_decode_tokens()
                        kwargs["token_data"] = user_data
                        return await func(*args, **kwargs)
                    case AuthEnum.CREATE.value:
                        find_user: List[
                            Record
                        ] = await UserRepository().find_user_by_email(
                            email=kwargs["form"].username
                        )
                        if find_user:
                            check_password = await hash.verify_password(
                                password=kwargs["form"].password,
                                old_password=find_user[0].get("hashed_password"),
                            )
                            if check_password:
                                tokens = self.create_tokens(
                                    user_id=find_user[0].get("id")
                                )
                                kwargs["tokens"] = tokens
                                return await func(*args, **kwargs)
                        await AuthExcp.no_create_tokens()
                    case AuthEnum.UPDATE.value:
                        try:
                            update_token = self.update_access_token(
                                refresh_token=kwargs["token"]
                            )
                            kwargs["token"] = update_token["Access-Token"]
                            return await func(*args, **kwargs)
                        except AttributeError:
                            await AuthExcp.no_update_token()
                    case _:
                        return await func(*args, **kwargs)

            return wrapper

        return func_wrapper
