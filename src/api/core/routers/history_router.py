from fastapi import APIRouter, status
from fastapi.requests import Request

# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import AllHistoriesSchema


history_router: APIRouter = APIRouter(
    prefix=APIRoutersData.HISTORY_ROUTER_PREFIX.value,
    tags=APIRoutersData.HISTORY_ROUTER_TAGS.value,
)


@history_router.get(
    path="/get_all_user_history",
    description="""Получение всей истории пользователя""",
    summary="История пользователя",
    response_model=AllHistoriesSchema,
    status_code=status.HTTP_200_OK,
)
async def get_all_user_history(request: Request) -> None:
    pass
