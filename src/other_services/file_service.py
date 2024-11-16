from fastapi import UploadFile
import aiofiles


class FileService:

    @classmethod
    async def save_file(cls, file: UploadFile, email: str) -> bool:
        try:
            async with aiofiles.open(
                "src/static/images/" + email + "_" + file.filename, "wb"
            ) as fl:
                await fl.write(file.file.read())
            return True
        except Exception:
            return False
