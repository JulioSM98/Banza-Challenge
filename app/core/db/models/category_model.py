from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from core.db.dabase_engine import Base


class Category(Base):
    __tablename__ = "Categoria"

    id = Column(Integer, primary_key=True, index=True)

    name = Column("nombre", String)
