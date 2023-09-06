from .base_crud import BaseCRUD

from core.db.models.client_model import Client
from core.schemas.client_schemas import ClientCreate


class ClientCRUD(BaseCRUD):
    def create_client(self, client: ClientCreate) -> Client:
        db_client = Client(**client.__dict__)
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def read_client_id(self, client_id: int) -> Client:
        return self.db.query(Client).filter(Client.id == client_id).first()

    def read_client_name(self, client_name: str) -> Client:
        return self.db.query(Client).filter(Client.name == client_name).first()

    def read_all_client(self, skip: int = 0, limit: int = 100):
        return self.db.query(Client).offset(skip).limit(limit).all()

    def update_client_id(self, client_id: int, client: ClientCreate) -> Client:
        db_client = self.read_client_id(client_id)
        db_client.name = client.name
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def delete_client_id(self, client_id: int) -> Client:
        db_client = self.read_client_id(client_id)
        self.db.delete(db_client)
        self.db.commit()
        return db_client
