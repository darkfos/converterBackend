from typing import Any, List, Union
from asyncpg import Pool


class GeneralRepository:
    def __init__(self, model, pool: Pool) -> None:
        self.model: Any = model
        self.pool = pool

    async def add_one(self, values: tuple) -> bool:
        async with self.pool as connection:
            try:
                stmt = f"INSERT INTO {await self.model.get_name()} {await self.model.get_columns()} VALUES {values}"
                await connection.execute(stmt)
            except Exception as ex:
                return False
            else:
                return True

    async def get_all(self):
        async with self.pool as connection:
            stmt = await connection.execute(
                f"SELECT * FROM {await self.model.get_name()}"
            )
            return stmt

    async def get_by_id(self, id_m: int) -> Union[None, Any]:
        async with self.pool as connection:
            stmt = f"SELECT * FROM {await self.model.get_name()} WHERE id = ${id_m}"
            return await connection.execute(stmt)

    async def update_by_id(self, id_m: int) -> bool:
        pass

    async def del_by_id(self, id_m: int) -> bool:
        async with self.pool as connection:
            try:
                stmt = f"DELETE FROM {await self.model.get_name()} WHERE id = ${id_m}"
                await connection.execute(stmt)
            except Exception as e:
                return False
            else:
                return True
