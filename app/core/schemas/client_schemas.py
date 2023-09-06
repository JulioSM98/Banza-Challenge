from pydantic import BaseModel
from typing import List
from .category_schemas import CategoryTable
from .account_schemas import AcccounId


class ClientBase(BaseModel):
    name: str


class ClientCreate(ClientBase):
    pass


class ClientTable(ClientBase):
    id: int


class AllClients(BaseModel):
    clients: List[ClientBase] = None


class ClientListCategory(BaseModel):
    category: CategoryTable


class OnlyClient(ClientTable):
    categorys: List[ClientListCategory]
    accounts: List[AcccounId]


class CategorysClient(BaseModel):
    categorys: List[ClientListCategory]


class AccountsClient(BaseModel):
    accounts: List[AcccounId]


class AccountBalance(BaseModel):
    id_account: int
    total: float
    total_usd: float
