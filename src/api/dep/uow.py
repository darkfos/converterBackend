# Local
from src.api.dep import IUOW
from src.db import UserTypeRepository, UserRepository, HistoryRepository
from src.db import UserModel, UserTypeModel, HistoryModel


class UOW(IUOW):

    async def __aenter__(self):

        self.user_rep = UserRepository(UserModel())
        self.user_t_rep = UserTypeRepository(UserTypeModel())
        self.history_rep = HistoryRepository(HistoryModel())

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        del self
