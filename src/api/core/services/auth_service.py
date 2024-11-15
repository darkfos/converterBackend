from typing import Dict, Union

from fastapi.security import OAuth2PasswordBearer

# Local
from src.api.auth import AuthService
from src.api.auth import HashService
from src.api.core.schemas import RegistrationUser, TokensSchema
from src.api.dep import UOW
from src.api.enums_sett import AuthEnum


auth: AuthService = AuthService()


class AuthAPIService:
    @staticmethod
    async def registration_user(user_data: RegistrationUser, uow: UOW) -> bool:
        async with uow:
            uow.user_rep.model.username = user_data.username
            uow.user_rep.model.email = user_data.email
            uow.user_rep.model.avatar = user_data.avatar
            uow.user_rep.model.hashed_password = await HashService.hash_password(password=user_data.password)

            return await uow.user_rep.add_one()

    @auth(type_token=AuthEnum.CREATE.value, hash=HashService)
    @staticmethod
    async def login_user(form: OAuth2PasswordBearer, uow: UOW, tokens: Dict[str, str] = {}) -> TokensSchema:
        return TokensSchema(
            access_token = tokens["Access-Token"],
            refresh_token = tokens["Refresh-Token"]
        )

    @auth(type_token=AuthEnum.UPDATE.value)
    @staticmethod
    async def update_token(token: str) -> str:
        return token