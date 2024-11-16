# Local
from src.db import HistoryModel
from src.db import GeneralRepository
from src.db import DbEngine


class HistoryRepository(GeneralRepository):
    def __init__(self, newModel: HistoryModel, testdb) -> None:
        self.model = newModel
        self.db = DbEngine() if not testdb else testdb
        super().__init__(model=self.model, pool=self.db)
