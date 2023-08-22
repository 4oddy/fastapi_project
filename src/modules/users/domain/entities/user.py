from dataclasses import dataclass
from typing import Optional

from src.common.entities import Entity
from src.common.services import generate_uuid


@dataclass
class User(Entity):
    id: str
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: int

    @staticmethod
    def create_user(
            username: str, first_name: str,
            last_name: str, age: int
    ) -> 'User':
        return User(
            id=generate_uuid(),
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age
        )
