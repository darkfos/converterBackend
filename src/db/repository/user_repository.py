from asyncpg import Connection, Record

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
            return await connection.fetch(
                f"SELECT * FROM users WHERE email = '{email}'"
            )

    async def get_all_information_about_user(self, id_user: int) -> Record:
        async with self.db as connection:
            return await connection.fetch(
                f"""
                SELECT * FROM users AS u
                INNER JOIN usertype AS us
                ON us.id = u.id_user_type
                WHERE u.id = {id_user}
                """
            )

    async def update_password(self, id_user: int, new_password: bytes) -> bool:
        async with self.db as connection:
            try:
                stmt = "UPDATE users SET hashed_password = $1 WHERE id = $2"
                await connection.execute(stmt, *(new_password, id_user))
                return True
            except Exception:
                return False
