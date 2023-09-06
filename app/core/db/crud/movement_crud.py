from .base_crud import BaseCRUD

from core.db.models.movement_model import Movement
from core.schemas.movement_schemas import MovementCreate


class MovementCRUD(BaseCRUD):
    def create_movement(self, movement: MovementCreate):
        db_movement = Movement(**movement.__dict__)
        self.db.add(db_movement)
        self.db.commit()
        self.db.refresh(db_movement)
        return db_movement

    def read_movement(self, movement_id: int):
        return self.db.query(Movement).filter(Movement.id == movement_id).first()

    def read_all_movement(self, id_account: int):
        return self.db.query(Movement).filter(Movement.id_account == id_account).all()

    def delete_movement(self, movement_id: int):
        db_movement = self.read_movement(movement_id)
        self.db.delete(db_movement)
        self.db.commit()
        return db_movement
