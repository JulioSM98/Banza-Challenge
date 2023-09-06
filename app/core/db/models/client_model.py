from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from core.db.dabase_engine import Base
from sqlalchemy.orm import Relationship


class Client(Base):
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True, index=True)
    name = Column("nombre", String)

    accounts = Relationship("Account", cascade="all,delete")
    categorys = Relationship("Client_Category", cascade="all,delete")
