from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from src.common.infrastructure.base_model import Model
from ..domain.entities.wish import Wish as WishEntity


class Wish(Model):
    __tablename__ = 'wish'

    title = Column(String(255), nullable=False)
    description = Column(String(), nullable=False)
    owner_id = Column(String(255), ForeignKey('user.id'))
    owner = relationship('User', back_populates='wishes')

    def to_entity(self) -> WishEntity:
        return WishEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            owner=self.owner.to_entity
        )

    @staticmethod
    def from_entity(entity: WishEntity) -> 'Wish':
        return Wish(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            owner_id=entity.owner.id
        )

