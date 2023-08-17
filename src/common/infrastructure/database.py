import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import Column

Base = declarative_base()


class Model(Base):
    __abstract__ = True

    created_at = Column(DateTime(), default=datetime.datetime.utcnow())
