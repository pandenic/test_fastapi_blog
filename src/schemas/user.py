import uuid

from fastapi_users import schemas
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserRead(schemas.BaseUser[uuid.UUID]):

    phone: PhoneNumber


class UserCreate(schemas.BaseUserCreate):

    phone: PhoneNumber
    

class UserUpdate(schemas.BaseUserUpdate):

    phone: PhoneNumber
