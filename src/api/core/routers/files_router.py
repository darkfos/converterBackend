from typing import Annotated

from fastapi import APIRouter, UploadFile, File, status, Depends
from fastapi.responses import FileResponse

from src.api.core.exceptions import FileExcp

# Local
from src.api.enums_sett import APIRoutersData
from src.api.auth import AuthService
from src.api.core.services import FileService


file_router: APIRouter = APIRouter(
    prefix=APIRoutersData.FILE_ROUTER_PREFIX.value,
    tags=APIRoutersData.FILE_ROUTER_TAGS.value,
)


@file_router.post(
    path="/convert_pdf_to_docx",
    description="""Конвертация pdf файла в docx""",
    summary="Конвертация pdf файла в docx",
    response_class=FileResponse,
    status_code=status.HTTP_201_CREATED,
)
async def convert_pdf_to_docx(
    token: Annotated[str, Depends(AuthService.convert_auth)],
    file_pdf: Annotated[UploadFile, File()],
) -> FileResponse:
    if file_pdf.filename.endswith(".pdf"):
        file_path = await FileService.convert_file_pdf_to_docx_file(
            file=file_pdf, token=token
        )
        return FileResponse(
            path="src/static/files/" + file_path, media_type="multipart/form-data"
        )
    await FileExcp.no_convert_to_docx_file()


@file_router.post(
    path="/convert_docx_to_pdf",
    description="""Конвертация docx файла в pdf""",
    summary="Конвертация docx в pdf",
    response_class=FileResponse,
    status_code=status.HTTP_201_CREATED,
)
async def convert_docx_to_pdf(
    token: Annotated[str, Depends(AuthService.convert_auth)],
    file_docx: Annotated[UploadFile, File()],
) -> FileResponse:
    if file_docx.filename.endswith(".docx"):
        file_path = await FileService.convert_file_docx_to_pdf_file(
            file=file_docx, token=token
        )

        return FileResponse(path=file_path, media_type="multipart/form-data")
    await FileExcp.no_convert_to_pdf_file()
