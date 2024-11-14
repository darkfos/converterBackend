# Local
from src.db import UserModel
from src.db import DbEngine
from src.db import GeneralRepository


class UserRepository(GeneralRepository):
    def __init__(self, newModel: UserModel) -> None:
        self.db = DbEngine()
        self.model = newModel
        super().__init__(model=self.model, pool=self.db)
