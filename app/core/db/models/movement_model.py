from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Enum, Numeric, DateTime
from core.db.dabase_engine import Base
import enum
import datetime


class Types_Movement(enum.Enum):
    ingreso = "income"
    egreso = "egress"


class Movement(Base):
    __tablename__ = "Movimiento"

    id = Column(Integer, primary_key=True, index=True)
    id_account = Column("id_cuenta", Integer, ForeignKey("Cuenta.id"))
    type = Column("tipo", Enum(Types_Movement))
    amount = Column("importe", Numeric(10, 2))
    date = Column("fecha", DateTime, default=datetime.datetime.now())
