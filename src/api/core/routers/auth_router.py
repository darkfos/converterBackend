from typing import Annotated

from fastapi import APIRouter, status, Depends, UploadFile, File, Form
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request
from fastapi.responses import Response
from pydantic import EmailStr, Field


# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import TokensSchema, RegistrationUser
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
    email: Annotated[EmailStr, Field(min_length=6)] = Form(),
    username: Annotated[str, Field(min_length=4, max_length=125)] = Form(),
    password: Annotated[str, Field(min_length=8)] = Form(),
    avatar: UploadFile = File(),
) -> None:
    result = await AuthAPIService.registration_user(
        user_data=RegistrationUser(email=email, username=username, password=password),
        uow=db_engine,
        avatar=avatar,
    )
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
    response: Response,
    db_engine: Annotated[IUOW, Depends(UOW)],
    form: OAuth2PasswordRequestForm = Depends(),
) -> TokensSchema:
    result = await AuthAPIService.login_user(form=form, uow=db_engine)
    response.set_cookie("access_key", result.access_token)
    response.set_cookie("refresh_key", result.refresh_token)
    return result


@auth_router.post(
    path="/update_token",
    description="""Обновление токена пользователя""",
    summary="Обновление токена",
    response_model=None,
    status_code=status.HTTP_200_OK,
)
async def update_access_token(request: Request, response: Response) -> None:
    new_token = await AuthAPIService.update_token(
        token=request.headers.get("refresh-token")
    )
    response.set_cookie("access_key", new_token)
    return None
