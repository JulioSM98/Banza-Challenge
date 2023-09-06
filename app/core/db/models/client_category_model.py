from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.orm import Relationship
from core.db.dabase_engine import Base


class Client_Category(Base):
    __tablename__ = "Categoria_Cliente"

    id_category = Column("id_categoria", Integer, ForeignKey("Categoria.id"), primary_key=True)
    id_client = Column("id_cliente", Integer, ForeignKey("Cliente.id"), primary_key=True)

    category = Relationship("Category")
    client = Relationship("Client", back_populates="categorys")
