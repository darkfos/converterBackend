from abc import abstractmethod, ABC

# Local
from src.db import UserTypeRepository, UserRepository, HistoryRepository


class IUOW(ABC):

    user_rep: UserRepository
    user_t_rep: UserTypeRepository
    history_rep: HistoryRepository

    @abstractmethod
    async def __aenter__(self):
        raise NotImplemented

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplemented
