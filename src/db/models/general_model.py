from abc import ABC, abstractmethod


class GeneralModel(ABC):

    @staticmethod
    @abstractmethod
    async def create_model():
        raise NotImplemented

    @abstractmethod
    async def get_values(self):
        raise NotImplemented

    @abstractmethod
    async def get_columns(self):
        raise NotImplemented

    @abstractmethod
    async def read_model(self):
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def get_name():
        raise NotImplemented
