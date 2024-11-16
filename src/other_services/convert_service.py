from typing import Union
from fastapi import UploadFile
from pdf2docx import Converter


# Local
from src.other_services import FileService


class ConvertService:

    @classmethod
    async def convert_pdf_to_docx(cls, pdf_file: UploadFile) -> Union[str, bool]:
        file_path: Union[str, bool] = await FileService.save_file_convert(file=pdf_file)
        if file_path:
            cv = Converter(pdf_file=file_path)
            cv.convert("src/static/files/DocxFile.docx", start=0, end=None)
            cv.close()
        return False