from typing import Dict, Union

import asyncpg

# Local
from src.api.dep import UOW
from src.api.auth import AuthService
from src.api.enums_sett import AuthEnum
from src.api.core.schemas.user_schemas import (
    AllUsersSchema,
    UserBaseSchema,
    AllInformationAboutUser,
)
from src.api.core.exceptions import UserExcp
from src.api.auth import HashService

auth: AuthService = AuthService()


class UserService:

    @staticmethod
    async def get_all_users(uow: UOW) -> AllUsersSchema:
        async with uow:
            all_users = await uow.user_rep.get_all()
            usersSchema = AllUsersSchema(users=[])
            for user in all_users:
                usersSchema.users.append(
                    UserBaseSchema(
                        email=user.get("email"), username=user.get("username")
                    )
                )
            return usersSchema

    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def get_information_about_me(
        uow: UOW, token: str = "", token_data: Dict[str, Union[str, int]] = {}
    ) -> AllInformationAboutUser:
        async with uow:
            try:
                res = await uow.user_rep.get_all_information_about_user(
                    id_user=token_data.get("sub")
                )
                if res:
                    return AllInformationAboutUser(
                        username=res[0].get("username"),
                        avatar=res[0].get("avatar"),
                        email=res[0].get("email"),
                        user_type_name=res[0].get("name_type"),
                    )
                await UserExcp.user_not_found()
            except asyncpg.EventTriggerProtocolViolatedError:
                await UserExcp.user_not_found()

    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def update_password(
        uow: UOW,
        new_password: str,
        token: str = "",
        token_data: Dict[str, Union[str, int]] = {},
    ) -> bool:
        async with uow:
            new_password = await HashService.hash_password(password=new_password)
            res = await uow.user_rep.update_password(
                id_user=token_data.get("sub"), new_password=new_password
            )
            return res

    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def delete_account(
        uow: UOW, token: str = "", token_data: Dict[str, Union[str, int]] = {}
    ) -> None:
        async with uow:
            res = await uow.user_rep.del_by_id(id_m=token_data.get("sub"))
            if res:
                return
            await UserExcp.no_delete_account()
