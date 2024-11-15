from typing import Dict, Union

# Local
from src.api.auth import AuthService
from src.api.auth import HashService
from src.api.core.schemas import RegistrationUser
from src.api.dep import UOW


class AuthAPIService:
    @staticmethod
    async def registration_user(user_data: RegistrationUser, uow: UOW) -> bool:
        async with uow:
            uow.user_rep.model.username = user_data.username
            uow.user_rep.model.email = user_data.email
            uow.user_rep.model.avatar = user_data.avatar
            uow.user_rep.model.hashed_password = await HashService.hash_password(password=user_data.password)

            return await uow.user_rep.add_one()