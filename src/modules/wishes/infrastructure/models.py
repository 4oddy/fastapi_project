import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from src.common.infrastructure.database import Model


class Wish(Model):
    __tablename__ = 'wish'

    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    description = Column(String(), nullable=False)
    owner_id = Column(String(255), ForeignKey('user.id'))
    owner = relationship('User', back_populates='wishes')
