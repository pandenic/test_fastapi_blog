import uuid
from typing import Any

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.db import get_async_session
from models.user import User


async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
) -> SQLAlchemyUserDatabase:
    yield SQLAlchemyUserDatabase[User, Any](session, User)


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.secret
    verification_token_secret = settings.secret

    async def on_after_register(
        self, user: User, request: Request | None = None,
    ) -> None:
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Request | None = None,
    ) -> None:
        print(
            f"User {user.id} has forgot their password. Reset token: {token}",
        )

    async def on_after_request_verify(
        self, user: User, token: str, request: Request | None = None,
    ) -> None:
        print(
            f"Verification requested for user {user.id}. "
            f"Verification token: {token}",
        )


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
) -> UserManager:
    yield UserManager(user_db)


cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy[models.UP, models.ID]:
    return JWTStrategy[models.UP, models.ID](
        secret=settings.secret, lifetime_seconds=3600,
    )


auth_backend = AuthenticationBackend[models.UP, models.ID](
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user(active=True)
current_anon_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(active=True, superuser=True)
