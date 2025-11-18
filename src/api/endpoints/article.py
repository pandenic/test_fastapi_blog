import logging
from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status

from core.db import NewAsyncSession
from core.users import current_user
from crud import crud_article
from models import Article, User
from schemas import CreateArticle, GetArticle, UpdateArticle
from services.minio import minio_service
from services.utils import execute_and_handle_api_exceptions

logger = logging.getLogger(__name__)

router = APIRouter()

CurrentUser = Annotated[User, Depends(current_user)]


@router.get("/")
async def get_all_articles(session: NewAsyncSession) -> list[GetArticle]:
    return await execute_and_handle_api_exceptions(
        crud_article.get_all(session),
        logger,
    )


@router.post("/")
async def create_article(
    article: CreateArticle,
    session: NewAsyncSession,
    user: CurrentUser,
) -> GetArticle:
    create_dict = article.model_dump()

    create_dict[Article.user_id.name] = user.id
    image_filename = await minio_service.upload_file_to_bucket(
        article.image, "article_",
    )
    create_dict[Article.image.name] = image_filename

    new_article = await execute_and_handle_api_exceptions(
        crud_article.create(session, create_dict),
        logger,
    )
    return new_article


@router.get("/{article_id}")
async def get_article(article_id: int, session: NewAsyncSession) -> GetArticle:
    article = await execute_and_handle_api_exceptions(
        crud_article.get_obj(session, article_id),
        logger,
    )
    

@router.patch("/{article_id}")
async def update_article(
    article_id: int,
    article: UpdateArticle,
    session: NewAsyncSession,
) -> GetArticle:
    return await execute_and_handle_api_exceptions(
        crud_article.update(
            session,
            article_id,
            article.model_dump(exclude_unset=True),
        ),
        logger,
    )


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: int, session: NewAsyncSession) -> None:
    return await execute_and_handle_api_exceptions(
        crud_article.mark_deleted(session, article_id),
        logger,
    )


@router.post("/upload_image")
async def upload_image(image: UploadFile) -> str:
    await minio_service.upload_file_to_bucket(image, "article_")
    return "OK"
