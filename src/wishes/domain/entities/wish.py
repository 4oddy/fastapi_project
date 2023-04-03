from dataclasses import dataclass

from common.entities import Entity

from .user import User


@dataclass
class Wish(Entity):
    id: int
    title: str
    description: str
    owner: User
