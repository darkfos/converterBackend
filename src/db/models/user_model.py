from typing import Tuple, Dict


# Local
from src.db import GeneralModel
from src.api.enums_sett import UserRole


class UserModel(GeneralModel):

    def __init__(
        self,
        email: str = None,
        name: str = None,
        password: str = None,
        avatar: str = None,
    ) -> None:
        self.id_user_type: int = UserRole.USER_ROLE.value
        self.email = email
        self.username = name
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
        email VARCHAR(200) UNIQUE,
        username VARCHAR(125),
        hashed_password BYTEA,
        avatar TEXT,
        FOREIGN KEY (id_user_type) REFERENCES UserType (id) ON DELETE CASCADE
        );
        """

    async def get_values(self) -> Tuple[int, str, str, str, str]:
        return (
            self.id_user_type,
            self.email,
            self.username,
            self.hashed_password,
            self.avatar,
        )

    async def get_columns(self) -> str:
        return "(" + ", ".join(self.__dict__.keys()) + ")"

    def __str__(self):
        return str({k: v for k, v in self.__dict__.items()})

    async def read_model(self) -> Dict[str, str]:
        return {k: v for k, v in self.__dict__.items()}
