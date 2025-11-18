from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import EmailStr

from core.config import email_settings

fast_email = FastMail(email_settings)

class EmailService:

    async def send_mail(self, emails: list[EmailStr], body: str) -> None:
        message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=emails,
            body=body,
            subtype=MessageType.html,
        )
        await fast_email.send_message(message)

email_service = EmailService()