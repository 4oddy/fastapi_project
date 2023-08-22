from typing import Optional

from src.common.commands import Command


class CreateUserCommand(Command):
    username: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: int
