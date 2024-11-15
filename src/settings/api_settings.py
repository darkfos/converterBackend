from os import getenv

from src.settings import DescriptorSettings
from dotenv import load_dotenv


load_dotenv()


class ApiSettings:

    API_PORT: DescriptorSettings = DescriptorSettings()
    JWT_SECRET_KEY: DescriptorSettings = DescriptorSettings()
    JWT_REFRESH_SECRET_KEY: DescriptorSettings = DescriptorSettings()
    SALT: DescriptorSettings = DescriptorSettings()

    def __init__(self) -> None:
        self.API_PORT = getenv("API_PORT")
        self.JWT_SECRET_KEY = getenv("TOKEN_KEY")
        self.JWT_REFRESH_SECRET_KEY = getenv("REFRESH_TOKEN_KEY")
        self.SALT = getenv("SALT")
