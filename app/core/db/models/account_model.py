from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.orm import Relationship
from core.db.dabase_engine import Base


class Account(Base):
    __tablename__ = "Cuenta"

    id = Column(Integer, primary_key=True, index=True)
    id_client = Column("id_cliente", Integer, ForeignKey("Cliente.id"))

    client = Relationship("Client", back_populates="accounts")
    movements = Relationship("Movement", cascade="all,delete")
