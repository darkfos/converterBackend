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
            data.update({"exp": datetime.now() + timedelta(minutes=api_settings.TIME_TOKEN_WORK)})
            access_token = jwt.encode(data, api_settings.JWT_SECRET_KEY, algorithm=api_settings.ALG)
            data["exp"] = (datetime.now() + timedelta(days=api_settings.TIME_REFRESH_WORK))
            refresh_token = jwt.encode(data, api_settings.JWT_REFRESH_SECRET_KEY, algorithm=api_settings.ALG)
            return {"Access-Token": access_token, "Refresh-Token": refresh_token}
        except jwt.PyJWTError:
            return False

    @classmethod
    def decode_tokens(cls, type_token: Literal["access", "decode"], token) -> str:
        try:
            match type_token:
                case "access":
                    return jwt.decode(jwt=token, key=api_settings.JWT_SECRET_KEY, algorithms=api_settings.ALG)
                case "decode":
                    return jwt.decode(jwt=token, key=api_settings.JWT_REFRESH_SECRET_KEY, algorithms=api_settings.ALG)
                case "_":
                    return ""
        except jwt.DecodeError:
            return ""