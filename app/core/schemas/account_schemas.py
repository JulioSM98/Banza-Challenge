from pydantic import BaseModel


class AccountBase(BaseModel):
    id_client: int


class AccountCreate(AccountBase):
    pass


class AcccounId(BaseModel):
    id: int


class AccountTable(AccountBase):
    id: int
