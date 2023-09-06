from pydantic import BaseModel
from .category_schemas import CategoryBase
from .client_schemas import ClientBase


class ClientCategoryBase(BaseModel):
    id_client: int
    id_category: int


class ClientCategoryCreate(ClientCategoryBase):
    pass


class ClientCategoryTable(ClientCategoryBase):
    pass


class ClientCategoryResponse(BaseModel):
    category: CategoryBase
    client: ClientBase
