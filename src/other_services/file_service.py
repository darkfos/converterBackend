from fastapi import UploadFile
from typing import Union
import aiofiles


class FileService:

    @classmethod
    async def save_file(cls, file: UploadFile, email: str) -> bool:
        try:
            async with aiofiles.open(
                "src/static/images/" + str(email) + "_" + file.filename, "wb"
            ) as fl:
                await fl.write(file.file.read())
            return True
        except Exception:
            return False

    @classmethod
    async def save_file_convert(cls, file: UploadFile) -> Union[bool, str]:
        try:
            async with aiofiles.open(
                "src/static/files/{}".format(file.filename), "wb"
            ) as fl:
                await fl.write(file.file.read())
            return "src/static/files/{}".format(file.filename)
        except Exception:
            return False
