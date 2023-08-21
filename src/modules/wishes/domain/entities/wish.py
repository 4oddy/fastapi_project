from dataclasses import dataclass

from src.common.entities import Entity
from src.modules.users.domain.entities.user import User


@dataclass
class Wish(Entity):
    id: str
    title: str
    description: str
    owner: User
