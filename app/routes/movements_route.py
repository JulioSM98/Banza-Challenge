from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.schemas.movement_schemas import MovementCreate, MovementBase
from dependencies import get_db
from utils.movements_utils import (
    create_movement_util,
    delete_movement_util,
    get_movement_util,
)

movements_router = APIRouter(prefix="/movements", tags=["🔃 Movimientos"])


@movements_router.post("/register", response_model=MovementBase)
def register_one_mevement_endpoint(movement: MovementCreate, db: Session = Depends(get_db)):
    return create_movement_util(db, movement)


@movements_router.delete("/{id_movement}/delete", response_model=MovementBase)
def delete_movement_endpoint(id_movement: int, db: Session = Depends(get_db)):
    return delete_movement_util(db, id_movement=id_movement)


@movements_router.get("/{id_movement}", response_model=MovementBase)
def get_movement_endpoint(id_movement: int, db: Session = Depends(get_db)):
    return get_movement_util(db, id_movement)
