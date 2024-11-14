from asyncpg import connection, Connection
import asyncio


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

        self.db_async_connector: Connection = await connection.connect()