from typing import TypeVar

from pydantic import BaseModel

from schemas.article import (  # noqa
    CreateArticle,
    GetArticle,
    ListArticle,
    UpdateArticle,
)
from schemas.category import Category  # noqa
from schemas.user import UserCreate, UserRead, UserUpdate  # noqa

SchemaModelType = TypeVar("SchemaModelType", bound=BaseModel)
