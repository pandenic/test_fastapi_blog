import asyncio
import logging

from pydantic import EmailStr

from services.celery.worker import celery_app
from services.email import email_service

logger = logging.getLogger(__name__)

@celery_app.task
def send_email(emails: list[EmailStr], message: str) -> None:
    try:
        asyncio.run(email_service.send_mail(emails, message))
    except Exception as e:
        logger.error(str(e))


