import uuid

from fastapi import UploadFile
from miniopy_async import Minio

from core.config import settings


class MinioService:

    def __init__(self) -> None:
        self.client = Minio(
            endpoint=settings.minio_endpoint,
            access_key=settings.minio_root_user,
            secret_key=settings.minio_root_password,
            secure=False,  # Disable SSL for local development
        )

    async def make_default_bucket_if_not_exist(self) -> None:
        if not await self.client.bucket_exists("default"):
            await self.client.make_bucket("default")

    async def upload_file_to_bucket(
        self, file: UploadFile, object_name_prefix: str, bucket_name: str = "default",
    ) -> str:
        object_name = f"images/{object_name_prefix}-{uuid.uuid4()}"
        await self.client.put_object(
            bucket_name,
            object_name,
            file,
            file.size,
            file.content_type,
        )
        return object_name

    async def get_obj_url(
        self, object_name: str, bucket_name: str = "default",
    ) -> str:
        return await self.client.presigned_get_object(bucket_name, object_name)

minio_service = MinioService()