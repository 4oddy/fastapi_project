from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column

from src.common.infrastructure.base_model import Model

from ..domain.entities.user import User as UserEntity


class User(Model):
    __tablename__ = 'user'

    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    age = Column(Integer())

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            username=self.username,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            age=self.age
        )

    @staticmethod
    def from_entity(entity: UserEntity) -> 'User':
        return User(
            id=entity.id,
            username=entity.username,
            password=entity.password,
            first_name=entity.first_name,
            last_name=entity.last_name,
            age=entity.age
        )
