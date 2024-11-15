from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request


# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import TokensSchema, RegistrationUser
from src.api.auth import AuthService
from src.api.core.services.auth_service import AuthAPIService
from src.api.dep import UOW, IUOW
from src.api.core.exceptions import AuthExcp


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
async def registration_user(
    request: Request,
    db_engine: Annotated[IUOW, Depends(UOW)],
    new_user: RegistrationUser
) -> None:
    result = await AuthAPIService.registration_user(user_data=new_user, uow=db_engine)
    if not result:
        await AuthExcp.no_reg_user()


@auth_router.post(
    path="/login",
    description="""Авторизация пользователя""",
    summary="Авторизация",
    response_model=TokensSchema,
    status_code=status.HTTP_200_OK,
)
async def login_user(
        request: Request,
        form: OAuth2PasswordRequestForm = Depends()) -> TokensSchema:
    pass


@auth_router.post(
    path="/update_token",
    description="""Обновление токена пользователя""",
    summary="Обновление токена",
    response_model=None,
    status_code=status.HTTP_200_OK,
)
async def update_access_token(
        request: Request,
        token: Annotated[str, Depends(AuthService.convert_auth)]
) -> None:
    pass
