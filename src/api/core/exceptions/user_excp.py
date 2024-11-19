from fastapi.exceptions import HTTPException
from fastapi import status

# Local
from src.api.enums_sett import APIRoutersData


class UserExcp:

    @classmethod
    async def user_not_found(cls) -> None:
        raise HTTPException(
            detail=f"""
            {APIRoutersData.USER_ROUTER_PREFIX.value}: Пользователь не был найден
            """,
            status_code=status.HTTP_404_NOT_FOUND,
        )

    @classmethod
    async def no_update_password(cls) -> None:
        raise HTTPException(
            detail=f"""
            {APIRoutersData.USER_ROUTER_PREFIX.value}: Не удалось обновить пароль
            """,
            status_code=status.HTTP_409_CONFLICT,
        )

    @classmethod
    async def no_update_avatar(cls) -> None:
        raise HTTPException(
            detail=f"""
            {APIRoutersData.USER_ROUTER_PREFIX.value}: Не удалось обновить аватар
            """,
            status_code=status.HTTP_409_CONFLICT,
        )

    @classmethod
    async def no_delete_account(cls) -> None:
        raise HTTPException(
            detail=f"""
            {APIRoutersData.USER_ROUTER_PREFIX.value}: Не удалось удалить аккаунт
            """,
            status_code=status.HTTP_409_CONFLICT,
        )
