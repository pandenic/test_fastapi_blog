from crud.base import CRUDBase
from models import Category


class CRUDCategory(CRUDBase):

    pass

crud_category = CRUDCategory(Category)
