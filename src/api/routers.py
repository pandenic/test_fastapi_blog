from fastapi import APIRouter

from api.endpoints.article import router as router_article
from api.endpoints.category import router as router_category
from api.endpoints.user import router as router_user

main_router = APIRouter()

main_router.include_router(router_article, prefix="/article", tags=["article"])
main_router.include_router(router_category, prefix="/category", tags=["category"])
main_router.include_router(router_user)
