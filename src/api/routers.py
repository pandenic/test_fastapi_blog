from fastapi import APIRouter

from api.endpoints import router_article, router_category

main_router = APIRouter()

main_router.include_router(router_article, prefix="/article")
main_router.include_router(router_category, prefix="/category")
