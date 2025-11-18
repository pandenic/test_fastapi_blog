from typing import TypeVar

from pydantic import BaseModel

from schemas.article import (  # noqa
    CreateArticleForm,
    GetArticle,
    UpdateArticle,
)
from schemas.category import CreateCategory, GetCategory  # noqa
from schemas.user import UserCreate, UserRead, UserUpdate  # noqa

SchemaModelType = TypeVar("SchemaModelType", bound=BaseModel)
