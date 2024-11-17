import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Local
from src.settings import api_settings
from src.api.core.routers import general_v1_router


class Application:

    def __init__(self):
        self.app = FastAPI(
            title=api_settings.title, description=api_settings.description
        )
        self.origins: list[str] = [
            "http://localhost:7565",
            "http://localhost:8080",
            "*",
        ]

    async def include_routers(self, routers: List[APIRouter]):
        for router in routers:
            self.app.include_router(router)

    def start_app(self) -> None:

        self.app.include_router(general_v1_router)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        uvicorn.run(self.app, workers=1, port=api_settings.API_PORT, host="0.0.0.0")
