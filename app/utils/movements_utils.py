from sqlalchemy.orm import Session
from fastapi import HTTPException

from core.db.crud.movement_crud import MovementCRUD
from core.db.crud.account_crud import AccountCRUD
from core.schemas.movement_schemas import MovementCreate
from .client_utils import calculate_account_util


def create_movement_util(db: Session, movement: MovementCreate):
    movement_crud = MovementCRUD(db)
    if validate_balanced_movement(db, movement):
        movement_db = movement_crud.create_movement(movement)
        return movement_db
    return None


def validate_balanced_movement(db: Session, movement: MovementCreate):
    account_crud = AccountCRUD(db)
    account_db = account_crud.read_account(movement.id_account)
    if account_db is None:
        raise HTTPException(status_code=404, detail="Account not found")
    if movement.type.value == "egress":
        total_balanced = calculate_account_util(account_db.movements, account_db.id)
        if total_balanced.total < movement.amount:
            raise HTTPException(status_code=400, detail="Exceeds available balance")
    return True


def delete_movement_util(db: Session, id_movement: int):
    movement_crud = MovementCRUD(db)
    if get_movement_util(db, id_movement) is None:
        raise HTTPException(status_code=404, detail="movement not found")
    return movement_crud.delete_movement(id_movement)


def get_movement_util(db: Session, id_movement: int):
    movement_crud = MovementCRUD(db)
    movement_db = movement_crud.read_movement(id_movement)
    if movement_db is None:
        raise HTTPException(status_code=404, detail="movement not found")
    return movement_db


def get_all_movement_account_util(db: Session, id_account: int):
    movement_crud = MovementCRUD(db)
    return movement_crud.read_all_movement(id_account)
