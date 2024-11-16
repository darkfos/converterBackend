from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.params import Query
from fastapi.responses import FileResponse
from starlette.requests import Request
from starlette.status import HTTP_204_NO_CONTENT

# Local
from src.api.enums_sett import APIRoutersData
from src.api.auth import AuthService
from src.api.dep import IUOW, UOW
from src.api.core.schemas import AllUsersSchema, AllInformationAboutUser
from src.api.core.services import UserService
from src.api.core.exceptions import UserExcp


user_router: APIRouter = APIRouter(
    prefix=APIRoutersData.USER_ROUTER_PREFIX.value,
    tags=APIRoutersData.USER_TYPE_ROUTER_TAGS.value,
)


@user_router.get(
    path="/get_all_users",
    description="""Получение всех пользователей""",
    summary="Список пользователей",
    status_code=status.HTTP_200_OK,
    response_model=AllUsersSchema,
)
async def get_all_users(
    uow: Annotated[IUOW, Depends(UOW)], request: Request
) -> AllUsersSchema:
    return await UserService.get_all_users(uow=uow)


@user_router.get(
    path="/information_about_me",
    description="""Получение данных о пользователе""",
    summary="Информация о пользователе",
    status_code=status.HTTP_200_OK,
    response_model=AllInformationAboutUser,
)
async def get_user_info(
    token: Annotated[str, Depends(AuthService.convert_auth)],
    uow: Annotated[IUOW, Depends(UOW)],
    request: Request,
) -> AllInformationAboutUser:
    return await UserService.get_information_about_me(uow=uow, token=token)


@user_router.get(
    path="/get_profile_image",
    description="""Получение изображение профиля""",
    summary="Изображение профиля",
    status_code=status.HTTP_200_OK,
    response_class=FileResponse,
)
async def get_profile_file(
    token: Annotated[str, Depends(AuthService.convert_auth)],
    uow: Annotated[IUOW, Depends(UOW)],
) -> FileResponse:
    src_file = await UserService.get_profile_avatar(uow=uow, token=token)
    return FileResponse(
        path=src_file,
        filename=src_file.split("_")[-1],
        media_type="multipart/form-data",
    )


@user_router.patch(
    path="/update_user_password",
    description="""Обновление пароля пользователя""",
    summary="Обновление пароля",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
async def update_username(
    uow: Annotated[IUOW, Depends(UOW)],
    token: Annotated[str, Depends(AuthService.convert_auth)],
    request: Request,
    new_password: Annotated[str, Query(min_length=8, max_length=125)],
) -> None:
    res = await UserService.update_password(
        uow=uow, token=token, new_password=new_password
    )
    if res:
        return
    await UserExcp.no_update_password()


@user_router.delete(
    path="/drop_account",
    description="""Удаление профиля пользователя""",
    summary="Удаление профиля",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_account_user(
    uow: Annotated[IUOW, Depends(UOW)],
    token: Annotated[str, Depends(AuthService.convert_auth)],
    request: Request,
) -> None:
    return await UserService.delete_account(uow=uow, token=token)
