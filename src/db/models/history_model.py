from typing import Tuple, Dict, Union
from datetime import datetime

# Local
from src.db import GeneralModel


class HistoryModel(GeneralModel):

    def __init__(
        self, name_operation: str = None, date_operation: datetime = None
    ) -> None:
        self.name_operation = name_operation
        self.date_operation = date_operation

    @staticmethod
    async def create_model() -> str:
        return """
        CREATE TABLE IF NOT EXISTS History (
        id SERIAL PRIMARY KEY,
        name_operation VARCHAR(255),
        date_operation DATE
        );
        """

    @staticmethod
    async def get_name():
        return "history"

    async def get_values(self) -> Tuple[str, datetime]:
        return (self.name_operation, self.date_operation)

    async def get_columns(self) -> str:
        return "(" + ", ".join(self.__dict__.keys()) + ")"

    def __str__(self) -> str:
        return str({k: v for k, v in self.__dict__.items()})

    async def read_model(self) -> Dict[str, Union[str, datetime]]:
        return {k: v for k, v in self.__dict__.items()}
