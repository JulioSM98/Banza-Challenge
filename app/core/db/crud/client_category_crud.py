from .base_crud import BaseCRUD

from core.db.models.client_category_model import Client_Category
from core.schemas.client_category_schemas import ClientCategoryCreate


class CientCategoryCRUD(BaseCRUD):
    def create_client_category(self, client_category: ClientCategoryCreate):
        db_client_category = Client_Category(**client_category.__dict__)
        self.db.add(db_client_category)
        self.db.commit()
        self.db.refresh(db_client_category)
        return db_client_category
