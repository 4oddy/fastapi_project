from dataclasses import dataclass
from typing import Optional

from src.common.entities import Entity


@dataclass
class User(Entity):
    id: str
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: int
