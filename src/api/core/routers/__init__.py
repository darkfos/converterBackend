__all__ = ["general_v1_router"]

from fastapi import APIRouter
from src.api.enums_sett import APIRoutersData
from src.api.core.routers.user_type_router import user_type_router
from src.api.core.routers.user_router import user_router
from src.api.core.routers.history_router import history_router
from src.api.core.routers.auth_router import auth_router
from src.api.core.routers.files_router import file_router


general_v1_router = APIRouter(
    prefix=APIRoutersData.API_V1_PREFIX.value, tags=APIRoutersData.API_V1_TAGS.value
)

# Include routers
general_v1_router.include_router(auth_router)
general_v1_router.include_router(user_type_router)
general_v1_router.include_router(user_router)
general_v1_router.include_router(history_router)
general_v1_router.include_router(file_router)
