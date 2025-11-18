from __future__ import annotations

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    
    phone: Mapped[str]
    tariff_id: Mapped[int | None] = mapped_column(ForeignKey("tariff.id"))

    # Relationships
    articles: Mapped[list["Article"] | None] = relationship(back_populates="user")  # noqa: F821
    tariff: Mapped["Tariff | None"] = relationship(back_populates="users")  # noqa: F821
