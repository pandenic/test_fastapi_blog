from typing import TypeVar

from models.article import Article, Category, Discount, Tariff  # noqa
from models.base import Base
from models.user import User  # noqa

SQLModelType = TypeVar("SQLModelType", bound=Base)
