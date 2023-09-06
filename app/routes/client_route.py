from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from core.schemas.client_schemas import (
    ClientBase,
    ClientCreate,
    ClientTable,
    OnlyClient,
    CategorysClient,
    AccountsClient,
    AccountBalance
)
from core.schemas.client_category_schemas import (
    ClientCategoryCreate,
    ClientCategoryResponse,
)
from utils.client_utils import (
    create_client_util,
    update_client_util,
    delete_client_util,
    get_all_clients_util,
    get_client_util,
    create_client_category_util,
    get_avalible_balance_util,
)

client_router = APIRouter(prefix="/client", tags=["👤 Clientes"])


@client_router.post("/create", response_model=ClientBase)
def create_client_endpoint(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client_util(db=db, client=client)


@client_router.put("/update/{client_id}", response_model=ClientBase)
def update_client_endpoint(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    return update_client_util(db=db, client_id=client_id, client=client)


@client_router.delete("/delete/{client_id}", response_model=ClientBase)
def delete_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    return delete_client_util(db, client_id)


@client_router.get("/get-all-clients", response_model=List[ClientTable])
def get_all_clients_endpoint(db: Session = Depends(get_db)):
    return get_all_clients_util(db)


@client_router.post("/add-client-category", response_model=ClientCategoryResponse)
def add_client_category(client_category: ClientCategoryCreate, db: Session = Depends(get_db)):
    return create_client_category_util(db, client_category)


@client_router.get("/{client_id}", response_model=OnlyClient)
def get_all_data_client(client_id: int, db: Session = Depends(get_db)):
    return get_client_util(db, client_id)


@client_router.get("/{client_id}/categorys", response_model=CategorysClient)
def get_categorys_client(client_id: int, db: Session = Depends(get_db)):
    return get_client_util(db, client_id)


@client_router.get("/{client_id}/accounts", response_model=AccountsClient)
def get_accounts_client(client_id: int, db: Session = Depends(get_db)):
    return get_client_util(db, client_id)


@client_router.get("/{client_id}/balance", response_model=List[AccountBalance])
def get_avalible_balance(client_id: int, db: Session = Depends(get_db)):
    return get_avalible_balance_util(db, client_id)
