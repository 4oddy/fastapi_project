import uuid

from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from src.common.infrastructure.database import Model


class User(Model):
    __tablename__ = 'user'

    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    age = Column(Integer())
    wishes = relationship('Wish', back_populates='owner')
