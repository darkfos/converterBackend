from fastapi import UploadFile
from typing import Dict, Union


# Local
from src.other_services import ConvertService
from src.other_services import CompressionService
from src.api.auth import AuthService
from src.api.enums_sett import AuthEnum
from src.api.core.exceptions import FileExcp


auth: AuthService = AuthService()


class FileService:

    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def convert_file_pdf_to_docx_file(
        file: UploadFile,
        token: str = "",
        token_data: Dict[str, Union[str, int]] = {},
    ) -> str:
        convert_file = await ConvertService.convert_pdf_to_docx(pdf_file=file)
        if convert_file:
            return convert_file
        await FileExcp.no_convert_to_docx_file()

    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def convert_file_docx_to_pdf_file(
        file: UploadFile, token: str = "", token_data: Dict[str, Union[str, int]] = {}
    ) -> str:
        convert_file = await ConvertService.convert_docx_to_pdf(docx_file=file)
        if convert_file:
            return convert_file
        await FileExcp.no_convert_to_pdf_file()

    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def compression_file(
        file: UploadFile, token: str = "", token_data: Dict[str, Union[str, int]] = {}
    ) -> Union[str, bool]:
        compress = await CompressionService.compression_file(file=file)
        return compress
