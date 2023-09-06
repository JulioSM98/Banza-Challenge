from sqlalchemy.orm import Session


class BaseCRUD:
    def __init__(self, db: Session) -> None:
        self.db = db
