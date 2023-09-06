from .base_crud import BaseCRUD

from core.db.models.account_model import Account
from core.schemas.account_schemas import AccountCreate


class AccountCRUD(BaseCRUD):
    def create_account(self, account: AccountCreate):
        db_account = Account(**account.__dict__)
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account

    def read_account(self, account_id: int):
        return self.db.query(Account).filter(Account.id == account_id).first()
