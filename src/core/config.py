from fastapi_mail import ConnectionConfig
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret: str

    article_image_available_file_type: list

    database_url: PostgresDsn

    rabbitmq_default_user: str
    rabbitmq_default_pass: str
    rabbitmq_host: str = "localhost"
    rabbitmq_port: int = 5672

    minio_endpoint: str
    minio_root_user: str
    minio_root_password: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="allow",
    )

class EmailSettings(ConnectionConfig):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="allow",
    )

settings = Settings()
email_settings = EmailSettings()
broker_url = (
    f"amqp://"
    f"{settings.rabbitmq_default_user}"
    f":{settings.rabbitmq_default_pass}"
    f"@{settings.rabbitmq_host}/"
)
