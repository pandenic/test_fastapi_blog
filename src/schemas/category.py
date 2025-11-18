from pydantic import BaseModel, PositiveInt


class BaseCategory(BaseModel):

    title: str

class CreateCategory(BaseCategory):

    pass

class GetCategory(BaseCategory):

    id: PositiveInt
