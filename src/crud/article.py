from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models import Article, SQLModelType
from schemas import SchemaModelType


class CRUDArticles(CRUDBase):

    async def update(
        self, session: AsyncSession, obj_id: int, schema: SchemaModelType,
    ) -> SQLModelType:
        query = (
            update(self.model)
            .where(self.model.id == obj_id)
            .values(**schema.model_dump())
        )
        obj = await session.execute(query)
        
        return obj.scalars().first()

    async def delete(self, session: AsyncSession, obj_id: int) -> None:
        obj = await session.get(self.model, obj_id)
        await session.delete(obj)
        await session.commit()


crud_article = CRUDArticles(Article)
