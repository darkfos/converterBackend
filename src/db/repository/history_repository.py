# Local
from asyncpg import Record, Connection
from typing import List

from src.db import HistoryModel
from src.db import GeneralRepository
from src.db import DbEngine


class HistoryRepository(GeneralRepository):
    def __init__(self, newModel: HistoryModel, testdb) -> None:
        self.model: HistoryModel = newModel
        self.db = DbEngine() if not testdb else testdb
        super().__init__(model=self.model, pool=self.db)

    async def get_all_by_us_id(self, id_user) -> List[Record]:
        async with self.db as connection:
            connection: Connection
            stmt: str = "SELECT * FROM history WHERE id_user = $1"
            return await connection.fetch(stmt, *(id_user,))
