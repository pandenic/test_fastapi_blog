from __future__ import annotations

import enum
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.user import User


class BillingPeriods(enum.Enum):

    PER_DAY = "per_day"
    PER_WEEK = "per_week"
    PER_MONTH = "per_month"
    PER_QUARTER = "per_quarter"
    PER_YEAR = "per_year"


class Category(Base):

    title: Mapped[str]

    # Relationships
    articles: Mapped[list["Article"]] = relationship(back_populates="category")


class Article(Base):

    title: Mapped[str]
    summary: Mapped[str]
    content: Mapped[str]
    image: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), server_onupdate=func.now(),
    )
    deleted: Mapped[bool] = mapped_column(default=False)

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    # Relationships
    user: Mapped[User] = relationship(back_populates="articles")
    category: Mapped[Category] = relationship(back_populates="articles")


class Discount(Base):

    title: Mapped[str]
    percent: Mapped[int]

    # Relationships
    tariffs: Mapped[list["Tariff"]] = relationship(back_populates="discount")


class Tariff(Base):
    
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[Decimal]
    billing_period: Mapped[BillingPeriods]
    discount_id: Mapped[int | None] = mapped_column(ForeignKey("discount.id"))

    # Relationships
    discount: Mapped[Discount | None] = relationship(back_populates="tariffs")
    users: Mapped[list[User]] = relationship(back_populates="tariff")
