from asyncpg import Connection

# Local
from src.db import UserModel
from src.db import DbEngine
from src.db import GeneralRepository


class UserRepository(GeneralRepository):
    def __init__(self, newModel: UserModel = UserModel()) -> None:
        self.db = DbEngine()
        self.model = newModel
        super().__init__(model=self.model, pool=self.db)

    async def find_user_by_email(self, email):
        async with self.db as connection:
            connection: Connection
            return await connection.fetch(f"SELECT * FROM users WHERE email = '{email}'")