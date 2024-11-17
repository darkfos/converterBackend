from fastapi.exceptions import HTTPException
from fastapi import status


# Local
from src.api.enums_sett import APIRoutersData


class FileExcp:

    @classmethod
    async def no_convert_to_docx_file(cls) -> None:
        raise HTTPException(
            detail=f"Ошибка: {APIRoutersData.FILE_ROUTER_PREFIX.value}. Не удалось конвертировать pdf файл в docx",  # noqa
            status_code=status.HTTP_409_CONFLICT,
        )

    @classmethod
    async def no_convert_to_pdf_file(cls) -> None:
        raise HTTPException(
            detail=f"Ошибка: {APIRoutersData.FILE_ROUTER_PREFIX.value}. Не удалось конвертировать docx файл в pdf", # noqa
            status_code=status.HTTP_409_CONFLICT,
        )
