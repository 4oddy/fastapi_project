import datetime

from sqlalchemy import Column, DateTime, String

from ..entities import Entity
from ..services import generate_uuid
from .database import Base


class Model(Base):
    __abstract__ = True

    id = Column(String(255), primary_key=True, default=generate_uuid)
    created_at = Column(DateTime(), default=datetime.datetime.utcnow)

    @staticmethod
    def from_entity(entity: Entity) -> 'Model':
        raise NotImplementedError
