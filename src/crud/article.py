from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from exceptions import ItemNotFoundError
from models import Article, Category


class CRUDArticles(CRUDBase):

    async def update(
        self, session: AsyncSession, obj_id: int, data: dict,
    ) -> Article:
        obj = await session.get(self.model, obj_id)
        if not obj:
            raise ItemNotFoundError(self.model)
        if category_id := data.get("category_id"):
            category = await session.get(Category, category_id)
            if not category:
                raise ItemNotFoundError(Category)
        await session.execute(
            update(self.model)
            .where(self.model.id == obj_id)
            .values(**data),
        )
        await session.commit()
        await session.refresh(obj)
        return obj

    async def mark_deleted(self, session: AsyncSession, obj_id: int) -> None:
        obj = await session.get(self.model, obj_id)
        if not obj:
            raise ItemNotFoundError(self.model)
        obj.deleted = True
        await session.commit()


crud_article = CRUDArticles(Article)
