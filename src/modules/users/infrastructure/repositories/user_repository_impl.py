from typing import Sequence

from sqlalchemy import delete, select, update

from ...domain.entities.user import User
from ..models import User as UserModel
from .user_repository import UserRepository


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
        user = UserModel.from_entity(entity)

        values_dict = entity.to_read_model().__dict__

        # remove empty items
        values_dict = {
            key: value for key, value in values_dict.items() if value
        }

        statement = update(
            UserModel
        ).filter_by(
            id=user.id
        ).values(
            values_dict
        ).returning(
            UserModel
        )

        mapping = self.session.execute(statement).mappings().one()
        return mapping['User'].to_entity()

    def delete_by_id(self, id_: str) -> str:
        statement = delete(
            UserModel
        ).filter_by(
            id=id_
        ).returning(
            *UserModel.__table__.columns
        )
        self.session.execute(statement)
        return id_
