from typing import Union
from fastapi import UploadFile
from pdf2docx import Converter
import pypandoc


# Local
from src.other_services import FileService
from src.other_services.cleaner_files import deletes_files


class ConvertService:

    @classmethod
    async def convert_pdf_to_docx(cls, pdf_file: UploadFile) -> Union[str, bool]:
        deletes_files()
        file_path: Union[str, bool] = await FileService.save_file_convert(file=pdf_file)
        if file_path:
            cv = Converter(pdf_file=file_path)
            cv.convert("src/static/files/DocxFile.docx", start=0, end=None)
            cv.close()
            return "DocxFile.docx"
        return False

    @classmethod
    async def convert_docx_to_pdf(cls, docx_file: UploadFile) -> Union[str, bool]:
        try:
            deletes_files()
            file_path: Union[str, bool] = await FileService.save_file_convert(
                file=docx_file
            )
            if file_path:
                pypandoc.convert_file(
                    file_path,
                    to="pdf",
                    outputfile=f"src/static/files/{docx_file.filename.split(".")[0]}.pdf", # noqa
                    extra_args=["--pdf-engine=xelatex"],
                )
                return f"src/static/files/{docx_file.filename.split(".")[0]}.pdf"
            return False
        except RuntimeError:
            return False
