from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routers import main_router
from services.minio import minio_service


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ANN201
    await minio_service.make_default_bucket_if_not_exist()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(main_router)

