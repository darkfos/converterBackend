import zlib
import aiofiles
from fastapi import UploadFile
from typing import Union, Final
from PyPDF2 import PdfReader, PdfWriter

# Local
from src.other_services.cleaner_files import deletes_files
from src.other_services import FileService


class CompressionService:

    @classmethod
    async def compression_file(cls, file: UploadFile) -> Union[str, bool]:
        deletes_files()
        try:
            new_file = zlib.compress(await file.read())
            new_filename = f"compress_{file.filename.split('.')[0]}.zlib"
            async with aiofiles.open(f"src/static/files/{new_filename}", "wb") as fl:
                await fl.write(new_file)
            return f"src/static/files/{new_filename}"
        except Exception:
            return False

    @classmethod
    async def compress_pdf_file(cls, file: UploadFile) -> Union[str, bool]:

        deletes_files()

        try:

            file_path = await FileService.save_file_convert(file=file)

            if file_path:

                pdf_reader: PdfReader = PdfReader(file_path)
                url_to_save: Final[str] = "src/static/files/compress/{}".format(
                    file.filename
                )
                pdf_writer: PdfWriter = PdfWriter()

                for page in range(0, len(pdf_reader.pages)):
                    page_compress = pdf_reader.pages[page]
                    page_compress.compress_content_streams()
                    pdf_writer.add_page(page_compress)

                with open(url_to_save, "wb") as fl:
                    pdf_writer.write(fl)
            else:
                raise ValueError

        except Exception:
            return False
        else:
            return url_to_save
