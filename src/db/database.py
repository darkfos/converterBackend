from asyncpg import Connection, create_pool

# Local
from src.settings import db_settings
from src.db import UserTypeModel, UserModel, HistoryModel


class DbEngine:
    __instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    async def __aenter__(self):
        self.db_async_connector: Connection = await create_pool(
            host=db_settings.DB_HOST,
            port=db_settings.DB_PORT,
            user=db_settings.DB_USER,
            password=db_settings.DB_PASSWORD,
            database=db_settings.DB_NAME,
        )

        await self.create_tables()

        return self.db_async_connector

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.db_async_connector.close()

    async def create_tables(self) -> None:
        async with self.db_async_connector.acquire() as connect:
            await connect.execute(await UserTypeModel.create_model())
            await connect.execute(await UserModel.create_model())
            await connect.execute(await HistoryModel.create_model())
