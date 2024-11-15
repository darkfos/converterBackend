from typing import Final

from fastapi import HTTPException, status


class AuthExcp:

    FROM: Final[str] = "/auth"

    @classmethod
    async def no_reg_user(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ошибка: {cls.FROM}. Не удалось зарегистрировать пользователя")

    @classmethod
    async def no_create_tokens(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ошибка: {cls.FROM}. Не удалось создать токены"
        )