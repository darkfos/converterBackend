from asyncpg import connection, Connection
import asyncio

# Local
from src.settings import db_settings
from src.db import UserTypeModel, UserModel, HistoryModel


class DbEngine:
    __instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        asyncio.run(self.connection_init())

    async def connection_init(self) -> None:
        """
        Установка подключения к БД
        :return:
        """

        self.db_async_connector: Connection = await connection.connect(
            host=db_settings.DB_HOST,
            port=db_settings.DB_PORT,
            user=db_settings.DB_USER,
            password=db_settings.DB_PASSWORD,
            database=db_settings.DB_NAME
        )
        await self.create_tables()

    async def create_tables(self) -> None:
        await self.db_async_connector.execute(await UserTypeModel.create_model())
        await self.db_async_connector.execute(await UserModel.create_model())
        await self.db_async_connector.execute(await HistoryModel.create_model())