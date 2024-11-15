import jwt
from typing import Dict, Final, Union, Literal
from datetime import timedelta, datetime

# Local
from src.settings import api_settings


class AuthService:

    @classmethod
    def create_tokens(cls, user_id: int) -> Union[bool, Dict[str, str]]:
        try:
            data = {"sub": user_id}
            data.update({"exp": datetime.utcnow() + timedelta(minutes=api_settings.TIME_TOKEN_WORK)})
            access_token = jwt.encode(data, api_settings.JWT_SECRET_KEY, algorithm=api_settings.ALG)
            data["exp"] = (datetime.utcnow() + timedelta(days=api_settings.TIME_REFRESH_WORK))
            refresh_token = jwt.encode(data, api_settings.JWT_REFRESH_SECRET_KEY, algorithm=api_settings.ALG)
            return {"Access-Token": access_token, "Refresh-Token": refresh_token}
        except jwt.PyJWTError:
            return False

    @classmethod
    def decode_tokens(cls, type_token: Literal["access", "refresh"], token) -> Union[Dict[str, Union[str, int]], bool]:
        try:
            match type_token:
                case "access":
                    return jwt.decode(
                        jwt=token,
                        key=api_settings.JWT_SECRET_KEY,
                        algorithms=api_settings.ALG,
                        options={"verify_exp": True}
                    )
                case "refresh":
                    return jwt.decode(
                        jwt=token,
                        key=api_settings.JWT_REFRESH_SECRET_KEY,
                        algorithms=api_settings.ALG,
                        options={"verify_exp": True}
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
            token_decode: Dict[str, str] = cls.decode_tokens(type_token="refresh", token=refresh_token)

            token_decode.update({"exp": datetime.utcnow() + timedelta(minutes=api_settings.TIME_TOKEN_WORK)})
            new_access_token = jwt.encode(
                payload=token_decode,
                key=api_settings.JWT_SECRET_KEY,
                algorithm=api_settings.ALG
            )

            return {"Access-Token": new_access_token}
        except jwt.DecodeError:
            return False
        except jwt.ExpiredSignatureError:
            return False