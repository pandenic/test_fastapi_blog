from fastapi import APIRouter, status

from core.db import NewAsyncSession
from crud import crud_article
from schemas import CreateArticle, GetArticle, UpdateArticle

router = APIRouter()


@router.get("/")
async def get_all_articles(session: NewAsyncSession) -> list[GetArticle]:
    return crud_article.get_all(session)


@router.post("/")
async def create_article(
    article: CreateArticle, session: NewAsyncSession,
) -> GetArticle:
    return crud_article.create(session, article)


@router.get("/{article_id}")
async def get_article(article_id: int, session: NewAsyncSession) -> GetArticle:
    return crud_article.get(session, article_id)


@router.patch("/{article_id}")
async def update_article(
    article_id: int, article: UpdateArticle, session: NewAsyncSession,
) -> GetArticle:
    return crud_article.update(session, article_id, article)

@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: int, session: NewAsyncSession) -> None:
    return

