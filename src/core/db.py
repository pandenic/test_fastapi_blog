from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings

engine = create_async_engine(str(settings.database_url), echo=True)

async_session_maker = async_sessionmaker[AsyncSession](engine)

async def get_async_session() -> AsyncSession:
    async with async_session_maker() as async_session:
        yield async_session


NewAsyncSession = Annotated[AsyncSession, Depends(get_async_session)]