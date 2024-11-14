from typing import Dict, Tuple


# Local
from src.db import GeneralModel


class UserTypeModel(GeneralModel):

    def __init__(self, name_type: str = None) -> None:
        self.name_type = name_type

    @staticmethod
    async def create_model() -> str:
        return """
        CREATE TABLE IF NOT EXISTS UserType (
        id SERIAL PRIMARY KEY,
        name_type VARCHAR(120)
        );
        """

    @staticmethod
    async def get_name() -> str:
        return "usertype"

    async def get_values(self) -> Tuple[str]:
        return (self.name_type,)

    async def get_columns(self):
        return "(" + ", ".join(self.__dict__.keys()) + ")"

    def __str__(self) -> str:
        return str({k: v for k, v in self.__dict__.items()})

    async def read_model(self) -> Dict[str, str]:
        return {k: v for k, v in self.__dict__.items()}
