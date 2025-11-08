from fastapi import APIRouter

from core.db import NewAsyncSession
from crud.category import crud_category
from schemas import Category

router = APIRouter()

@router.get("/")
async def get_categories(session: NewAsyncSession) -> list[Category]:
    return crud_category.get_all(session)

@router.create("/")
async def create_category(category: Category, session: NewAsyncSession) -> Category:
    return crud_category.create(session, category)
