from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from exceptions import ItemNotFoundError
from models import SQLModelType


class CRUDBase:
    def __init__(self, model: SQLModelType) -> None:
        self.model = model

    async def create(
        self, session: AsyncSession, data: dict,
    ) -> SQLModelType:
        obj = self.model(**data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def get_all(self, session: AsyncSession) -> list[SQLModelType]:
        objs = await session.execute(select(self.model))
        if not objs:
            raise ItemNotFoundError(self.model)
        return objs.scalars().all()

    async def get_obj(
        self,
        session: AsyncSession,
        obj_id: int,
    ) -> SQLModelType:
        obj = await session.get(self.model, obj_id)
        if not obj:
            raise ItemNotFoundError(self.model)
        return obj
