from __future__ import annotations

from fastapi import HTTPException, status

from core.config import settings
from models import SQLModelType


class UserDeleteForbiddenError(HTTPException):
    def __init__(self) -> None:
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        detail = "User deleting is forbidden!"
        super().__init__(status_code, detail)


class ItemNotFoundError(HTTPException):
    def __init__(self, model: SQLModelType) -> None:
        status_code = status.HTTP_404_NOT_FOUND
        detail = f"{model.__name__} not found"
        super().__init__(status_code, detail)

class WrongArticleImageFormatError(HTTPException):
    def __init__(self, model: SQLModelType) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        detail = (
            f"Wrong image format. It should be one of "
            f"{settings.article_image_available_file_type}"
        )
        super().__init__(status_code, detail)

