from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import SQLModelType
from schemas import SchemaModelType


class CRUDBase:
    def __init__(self, model: SQLModelType) -> None:
        self.model = model

    async def create(
        self, session: AsyncSession, schema: SchemaModelType,
    ) -> SQLModelType:
        obj = self.model(**schema.model_dump())
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def get_all(self, session: AsyncSession) -> list[SQLModelType]:
        return await session.scalars(select(self.model)).all()

    async def get_obj(
        self,
        session: AsyncSession,
        obj_id: int,
    ) -> SQLModelType:
        return await session.get(self.model, obj_id)
