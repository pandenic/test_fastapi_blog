from datetime import datetime
from typing import Annotated
from uuid import UUID

from fastapi import Form, UploadFile
from fastapi.background import P
from pydantic import BaseModel, ConfigDict, PositiveInt, field_validator

from core.config import settings
from exceptions import WrongArticleImageFormatError


class BaseArticle(BaseModel):
    
    title: str
    summary: str
    content: str
    category_id: PositiveInt

class GetArticle(BaseArticle):

    id: PositiveInt
    created_at: datetime
    updated_at: datetime

    deleted: bool = False

    user_id: UUID

    model_config = ConfigDict(from_attributes=True)


class CreateArticle(BaseArticle):
    
    pass


CreateArticleForm = Annotated[CreateArticle, Form()]


class UpdateArticle(BaseArticle):

    title: str | None = None
    summary: str | None = None
    content: str | None = None
    image: str | None = None
    category_id: PositiveInt | None = None
