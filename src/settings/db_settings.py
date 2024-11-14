from os import getenv
from dotenv import load_dotenv
from src.settings import DescriptorSettings


load_dotenv()


class DatabaseSettings:

    DB_HOST: DescriptorSettings = DescriptorSettings()
    DB_PORT: DescriptorSettings = DescriptorSettings()
    DB_NAME: DescriptorSettings = DescriptorSettings()
    DB_USER: DescriptorSettings = DescriptorSettings()
    DB_PASSWORD: DescriptorSettings = DescriptorSettings()

    def __init__(self) -> None:
        self.DB_HOST = getenv("DB_HOST")
        self.DB_PORT = getenv("DB_PORT")
        self.DB_NAME = getenv("DB_NAME")
        self.DB_USER = getenv("DB_USER")
        self.DB_PASSWORD = getenv("DB_PASSWORD")