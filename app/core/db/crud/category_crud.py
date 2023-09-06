from .base_crud import BaseCRUD

from core.db.models.category_model import Category
from core.schemas.category_schemas import CategoryCreate


class CategoryCRUD(BaseCRUD):
    def create_category(self, category: CategoryCreate) -> Category:
        db_category = Category(**category.__dict__)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def read_category_id(self, category_id: int):
        return self.db.query(Category).filter(Category.id == category_id).first()

    def read_all_category(self, skip: int = 0, limit: int = 100):
        return self.db.query(Category).offset(skip).offset(limit).all()
