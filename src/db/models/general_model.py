from abc import ABC, abstractmethod


class GeneralModel(ABC):

    @staticmethod
    @abstractmethod
    async def create_model():
        raise NotImplementedError

    @abstractmethod
    async def get_values(self):
        raise NotImplementedError

    @abstractmethod
    async def get_columns(self):
        raise NotImplementedError

    @abstractmethod
    async def read_model(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def get_name():
        raise NotImplementedError
