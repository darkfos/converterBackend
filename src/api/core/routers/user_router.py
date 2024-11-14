from fastapi import APIRouter, status
from starlette.requests import Request
from starlette.status import HTTP_204_NO_CONTENT

# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import UserBaseSchema, AllUsersSchema


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
async def get_all_users(request: Request) -> AllUsersSchema:
    pass


@user_router.get(
    path="/information_about_me",
    description="""Получение данных о пользователе""",
    summary="Информация о пользователе",
    status_code=status.HTTP_200_OK,
    response_model=UserBaseSchema,
)
async def get_user_by_id(request: Request) -> UserBaseSchema:
    pass


@user_router.put(
    path="/update_user_password",
    description="""Обновление пароля пользователя""",
    summary="Обновление пароля",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
async def update_user(request: Request) -> None:
    pass


@user_router.delete(
    path="/drop_account",
    description="""Удаление профиля пользователя""",
    summary="Удаление профиля",
    status_code=HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_account_user(request: Request) -> None:
    pass
