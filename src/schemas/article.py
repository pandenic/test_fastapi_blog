import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Article(BaseModel):
    
    title: str
    summary: str
    content: str
    picture: str | None
    category_id: int

    model_config = ConfigDict(from_attributes=True)

class GetArticle(Article):

    created_at: datetime
    updated_at: datetime

    deleted: bool

    user_id: UUID


class CreateArticle(Article):
    
    user_id: UUID

class UpdateArticle(Article):

    title: str
    summary: str
    content: str
    picture: str | None
    category_id: int
