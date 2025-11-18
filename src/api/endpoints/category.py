import logging

from fastapi import APIRouter

from core.db import NewAsyncSession
from crud import crud_category
from schemas import CreateCategory, GetCategory
from services.utils import execute_and_handle_api_exceptions

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/")
async def get_categories(session: NewAsyncSession) -> list[GetCategory]:
    return await execute_and_handle_api_exceptions(
        crud_category.get_all(session),
        logger,
    )


@router.post("/")
async def create_category(
    category: CreateCategory,
    session: NewAsyncSession,
) -> GetCategory:
    return await execute_and_handle_api_exceptions(
        crud_category.create(session, category),
        logger,
    )
