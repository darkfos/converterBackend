from typing import Annotated

from fastapi import APIRouter, UploadFile, File, status, Depends
from fastapi.responses import FileResponse


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
    status_code=status.HTTP_201_CREATED
)
async def convert_pdf_to_docx(
    token: Annotated[str, Depends(AuthService.convert_auth)],
    file_pdf: Annotated[UploadFile, File()],
) -> FileResponse:
    file_path = await FileService.convert_file_pdf_to_docx_file(
        file=file_pdf, token=token
    )
    return FileResponse(
        path="src/static/files/" + file_path, media_type="multipart/form-data"
    )
