from dataclasses import dataclass
from common.entities import Entity

from modules.users.domain.entities.user import User


@dataclass
class Wish(Entity):
    id: str
    title: str
    description: str
    owner: User
