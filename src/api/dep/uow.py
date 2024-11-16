# Local
from src.api.dep import IUOW
from src.db import UserTypeRepository, UserRepository, HistoryRepository
from src.db import UserModel, UserTypeModel, HistoryModel


class UOW(IUOW):

    async def __aenter__(self, testdb = None):

        self.user_rep = UserRepository(UserModel(), testdb=testdb if testdb else None)
        self.user_t_rep = UserTypeRepository(UserTypeModel(), testdb=testdb if testdb else None)
        self.history_rep = HistoryRepository(HistoryModel(), testdb=testdb if testdb else None)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        del self
