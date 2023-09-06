from pydantic import BaseModel
from core.db.models.movement_model import Types_Movement


class MovementBase(BaseModel):
    id_account: int
    type: Types_Movement
    amount: int


class MovementCreate(MovementBase):
    pass

