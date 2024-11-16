from os import getenv

from src.settings import DescriptorSettings
from dotenv import load_dotenv


load_dotenv()


class ApiSettings:

    API_PORT: DescriptorSettings = DescriptorSettings()
    JWT_SECRET_KEY: DescriptorSettings = DescriptorSettings()
    TIME_TOKEN_WORK: DescriptorSettings = DescriptorSettings()
    JWT_REFRESH_SECRET_KEY: DescriptorSettings = DescriptorSettings()
    TIME_REFRESH_WORK: DescriptorSettings = DescriptorSettings()
    SALT: DescriptorSettings = DescriptorSettings()
    ALG: DescriptorSettings = DescriptorSettings()

    def __init__(self) -> None:
        self.API_PORT = int(getenv("API_PORT"))
        self.JWT_SECRET_KEY = getenv("TOKEN_KEY")
        self.TIME_TOKEN_WORK = int(getenv("TOKEN_TIME_WORK"))
        self.JWT_REFRESH_SECRET_KEY = getenv("REFRESH_TOKEN_KEY")
        self.TIME_REFRESH_WORK = int(getenv("REFRESH_TIME_WORK"))
        self.ALG = getenv("ALG")

        # Other
        self.title: str = "ConvertApp"
        self.description: str = "Серверная часть веб приложения ConvertApp"
