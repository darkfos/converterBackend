from fastapi import APIRouter, status
from fastapi.requests import Request


# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import TokensSchema


auth_router: APIRouter = APIRouter(
    prefix=APIRoutersData.AUTH_PREFIX.value, tags=APIRoutersData.AUTH_TAGS.value
)


@auth_router.post(
    path="/register",
    description="""Регистрация пользователя""",
    summary="Регистрация",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def registration_user(request: Request) -> None:
    pass


@auth_router.post(
    path="/login",
    description="""Авторизация пользователя""",
    summary="Авторизация",
    response_model=TokensSchema,
    status_code=status.HTTP_200_OK,
)
async def login_user(request: Request) -> TokensSchema:
    pass


@auth_router.post(
    path="/update_token",
    description="""Обновление токена пользователя""",
    summary="Обновление токена",
    response_model=None,
    status_code=status.HTTP_200_OK,
)
async def update_access_token(request: Request) -> None:
    pass
