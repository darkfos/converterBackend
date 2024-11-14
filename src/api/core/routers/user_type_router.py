from fastapi import APIRouter, Request

# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import AllUserTypes, UserTypeBaseSchema


user_type_router: APIRouter = APIRouter(
    prefix=APIRoutersData.USER_TYPE_ROUTER_PREFIX.value,
    tags=APIRoutersData.USER_TYPE_ROUTER_TAGS.value,
)


@user_type_router.get(
    path="/get_all_user_types",
    description="""Получение всех типов пользователей""",
    summary="Типы пользователей",
    response_model=AllUserTypes,
)
async def get_all_user_types(request: Request) -> AllUserTypes:
    pass


@user_type_router.get(
    path="/get_user_type/{id_u}",
    description="""Получение типа пользователя по id""",
    summary="Получение типа пользователя по id",
    response_model=UserTypeBaseSchema,
)
async def get_user_type_by_id(id_u: int, request: Request) -> UserTypeBaseSchema:
    print(id_u)
