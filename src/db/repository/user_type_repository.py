# Local
from src.db import GeneralRepository
from src.db import UserTypeModel
from src.db import DbEngine


class UserTypeRepository(GeneralRepository):
    def __init__(self, newModel: UserTypeModel) -> None:
        self.model = newModel
        self.db = DbEngine()
        super().__init__(model=self.model, pool=self.db)
