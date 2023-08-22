from typing import Sequence

from sqlalchemy import select, delete

from .user_repository import UserRepository
from ..models import User as UserModel
from ...domain.entities.user import User


class UserRepositoryImpl(UserRepository):
    def find_by_username(self, username: str) -> User | None:
        statement = select(UserModel).filter_by(username=username)
        user = self.session.execute(statement).scalar_one()
        return user.to_entity()

    def create(self, entity: User) -> User:
        user = UserModel.from_entity(entity)
        self.session.add(user)
        return user.to_entity()

    def findall(self) -> Sequence[User]:
        users = self.session.query(UserModel).all()
        return [
            user.to_entity() for user in users
        ]

    def find_by_id(self, id_: str) -> User | None:
        user = self.session.get(UserModel, id_)

        if user is None:
            return None

        return user.to_entity()

    def update(self, entity: User) -> User:
        ...

    def delete_by_id(self, id_: str) -> User:
        ...
