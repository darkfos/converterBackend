import uvicorn
from fastapi import FastAPI, APIRouter
from typing import List

# Local
from src.settings import api_settings
from src.api.core.routers import general_v1_router


class Application:

    def __init__(self):
        self.app = FastAPI(
            title=api_settings.title, description=api_settings.description
        )

    async def include_routers(self, routers: List[APIRouter]):
        for router in routers:
            self.app.include_router(router)

    def start_app(self) -> None:

        self.app.include_router(general_v1_router)
        uvicorn.run(self.app, workers=1, port=api_settings.API_PORT, host="0.0.0.0")
