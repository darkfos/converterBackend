from typing import Dict

from fastapi import UploadFile
from fastapi.security import OAuth2PasswordBearer

# Local
from src.api.auth import AuthService
from src.api.auth import HashService
from src.api.core.exceptions import AuthExcp
from src.api.core.schemas import RegistrationUser, TokensSchema
from src.api.dep import UOW
from src.api.enums_sett import AuthEnum
from src.other_services import FileService


auth: AuthService = AuthService()


class AuthAPIService:
    @staticmethod
    async def registration_user(
        user_data: RegistrationUser, uow: UOW, avatar: UploadFile
    ) -> bool:

        # Save file
        res_save_file: bool = await FileService.save_file(
            file=avatar, email=user_data.email
        )

        if not res_save_file:
            await AuthExcp.no_reg_user()
        async with uow:
            uow.user_rep.model.username = user_data.username
            uow.user_rep.model.email = user_data.email
            uow.user_rep.model.avatar = (
                "src/static/images/{}_".format(user_data.email) + avatar.filename
            )
            uow.user_rep.model.hashed_password = await HashService.hash_password(
                password=user_data.password
            )

            return await uow.user_rep.add_one()

    @auth(type_token=AuthEnum.CREATE.value, hash=HashService)
    @staticmethod
    async def login_user(
        form: OAuth2PasswordBearer, uow: UOW, tokens: Dict[str, str] = {}
    ) -> TokensSchema:
        return TokensSchema(
            access_token=tokens["Access-Token"], refresh_token=tokens["Refresh-Token"]
        )

    @auth(type_token=AuthEnum.UPDATE.value, is_refresh=True)
    @staticmethod
    async def update_token(token: str = "") -> str:
        return token
