import copy
from dataclasses import dataclass
from typing import Optional

from src.common.entities import Entity
from src.common.services import generate_uuid


@dataclass
class UserBaseAttrsMixin:
    id: str
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: int


@dataclass
class UserReadModel(UserBaseAttrsMixin):
    ...


@dataclass
class User(Entity, UserBaseAttrsMixin):
    password: str

    @staticmethod
    def create_user(
            username: str, first_name: str, password: str,
            last_name: str, age: int
    ) -> 'User':
        return User(
            id=generate_uuid(),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age
        )

    def to_read_model(self) -> UserReadModel:
        user_prototype = copy.deepcopy(self)
        user_prototype.__dict__.pop('password')
        return UserReadModel(**user_prototype.__dict__)
