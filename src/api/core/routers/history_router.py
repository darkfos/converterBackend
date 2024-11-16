from typing import Annotated

from fastapi import APIRouter, status
from fastapi.params import Depends
from fastapi.requests import Request

# Local
from src.api.enums_sett import APIRoutersData
from src.api.core.schemas import AllHistoriesSchema, BaseHistorySchema
from src.api.core.services.history_service import HistoryService
from src.api.auth import AuthService
from src.api.dep import IUOW, UOW


history_router: APIRouter = APIRouter(
    prefix=APIRoutersData.HISTORY_ROUTER_PREFIX.value,
    tags=APIRoutersData.HISTORY_ROUTER_TAGS.value,
)


@history_router.post(
    path="/create_history",
    description="""Создание истории пользователя""",
    summary="Создание истории",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_history(
        new_history: BaseHistorySchema,
        db_engine: Annotated[IUOW, Depends(UOW)],
        token: Annotated[str, Depends(AuthService.convert_auth)],
        request: Request
) -> None:
    await HistoryService.create_history(
        new_history=new_history,
        uow=db_engine,
        token=token
    )

@history_router.get(
    path="/get_all_user_history",
    description="""Получение всей истории пользователя""",
    summary="История пользователя",
    response_model=AllHistoriesSchema,
    status_code=status.HTTP_200_OK,
)
async def get_all_user_history(
        token: Annotated[str, Depends(AuthService.convert_auth)],
        db_engine: Annotated[IUOW, Depends(UOW)],
        request: Request
) -> None:
    return await HistoryService.get_all_histories_for_user(
        uow=db_engine,
        token=token,
    )
