from sqlalchemy.orm import Session
from fastapi import HTTPException
from core.schemas.client_schemas import ClientCreate, AccountBalance
from core.db.crud.client_crud import ClientCRUD, Client
from core.db.crud.category_crud import CategoryCRUD
from core.schemas.client_category_schemas import ClientCategoryCreate
from core.db.crud.client_category_crud import CientCategoryCRUD
from core.db.crud.account_crud import AccountCRUD
from core.schemas.account_schemas import AccountCreate
import httpx


def create_client_util(db: Session, client: ClientCreate):
    client_crud = ClientCRUD(db)
    if client_crud.read_client_name(client.name) is not None:
        raise HTTPException(status_code=400, detail="Client already registered")
    db_client = client_crud.create_client(client)
    create_account_util(db, db_client.id)
    return db_client


def create_account_util(db: Session, id_client: int):
    db_account = AccountCreate(id_client=id_client)
    account_crud = AccountCRUD(db)
    return account_crud.create_account(db_account)


def get_client_util(db: Session, client_id: int):
    client_crud = ClientCRUD(db)
    client_db = client_crud.read_client_id(client_id)
    if client_db is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_db


def get_client_name_util(db: Session, client_name: str):
    client_crud = ClientCRUD(db)
    return client_crud.read_client_name(client_name)


def update_client_util(db: Session, client_id: int, client: ClientCreate):
    client_crud = ClientCRUD(db)
    if client_crud.read_client_id(client_id) is None:
        raise HTTPException(status_code=404, detail="Client not found")
    if client_crud.read_client_name(client.name) is not None:
        raise HTTPException(status_code=400, detail="Client Name already registered")
    return client_crud.update_client_id(client_id, client)


def delete_client_util(db: Session, client_id: int):
    client_crud = ClientCRUD(db)
    if client_crud.read_client_id(client_id) is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_crud.delete_client_id(client_id)


def get_all_clients_util(db: Session):
    client_crud = ClientCRUD(db)
    return client_crud.read_all_client()


def create_client_category_util(db: Session, client_category: ClientCategoryCreate):
    client_category_crud = CientCategoryCRUD(db)
    db_client = get_client_util(db, client_category.id_client)
    db_client_category = get_category(db, client_category.id_category)
    for category in db_client.categorys:
        if category.id_category == client_category.id_category:
            raise HTTPException(status_code=400, detail="Client already in category")
    if db_client is not None and db_client_category is None:
        raise HTTPException(status_code=404, detail="Client o Category not found")
    return client_category_crud.create_client_category(client_category)


def get_category(db: Session, id_category: int):
    category_crud = CategoryCRUD(db)
    return category_crud.read_category_id(id_category)


def get_avalible_balance_util(db: Session, id_client: int):
    db_client = get_client_util(db, id_client)
    if count_movements(db_client) == 0:
        raise HTTPException(status_code=400, detail="The customer has no movement")
    accounts_list = [calculate_account_util(data.movements, data.id) for data in db_client.accounts]

    return accounts_list


def count_movements(db_client: Client):
    total = 0
    for account in db_client.accounts:
        total += len(account.movements)
    return total


def calculate_account_util(list_movements: list, id_account: int) -> AccountBalance:
    total = 0
    for movement in list_movements:
        if movement.type.value == "income":
            total += float(movement.amount)
        else:
            total -= float(movement.amount)
    total_usd = get_total_usd(total)
    return AccountBalance(id_account=id_account, total=total, total_usd=total_usd)


def get_total_usd(total: float):
    total_usd = 0
    api_dolar = httpx.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales").json()
    for value in api_dolar:
        if value.get("casa").get("nombre") == "Dolar Bolsa":
            total_usd = total / float(value.get("casa").get("compra").replace(",", "."))
            break
    return total_usd
