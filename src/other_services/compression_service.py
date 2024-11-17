import zlib
import aiofiles
from fastapi import UploadFile
from typing import Union


# Local
from src.other_services.cleaner_files import deletes_files


class CompressionService:

    @classmethod
    async def compression_file(cls, file: UploadFile) -> Union[str, bool]:
        deletes_files()
        try:
            new_file = zlib.compress(await file.read())
            async with aiofiles.open(
                f"src/static/files/{"compress_"+file.filename.split(".")[0]}.zlib", "wb" # noqa
            ) as fl:
                await fl.write(new_file)
            return f"src/static/files/{"compress_"+file.filename.split(".")[0]}.zlib"
        except Exception:
            return False
