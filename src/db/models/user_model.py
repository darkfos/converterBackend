from typing import Tuple, Dict


# Local
from src.db import GeneralModel


class UserModel(GeneralModel):

    def __init__(self, email: str = None, name: str = None, password: str = None, avatar: str = None) -> None:
        self.email = email
        self.name = name
        self.hashed_password = password
        self.avatar = avatar

    @staticmethod
    async def get_name() -> str:
        return "users"

    @staticmethod
    async def create_model() -> str:
        return """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        id_user_type INTEGER,
        email VARCHAR(200),
        hashed_password VARCHAR(125),
        avatar TEXT,
        FOREIGN KEY (id_user_type) REFERENCES UserType (id) ON DELETE CASCADE
        );
        """

    async def get_values(self) -> Tuple[str, str, str, str]:
        return (self.email, self.name, self.hashed_password, self.avatar)

    async def get_columns(self) -> str:
        return "(" + ", ".join(self.__dict__.keys()) + ")"

    def __str__(self):
        return str({
            k: v
            for k, v in self.__dict__.items()
        })

    async def read_model(self) -> Dict[str, str]:
        return {
            k: v
            for k, v in self.__dict__.items()
        }