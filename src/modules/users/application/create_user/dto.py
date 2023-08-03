from typing import Optional

from common.commands import Command


class CreateUserCommand(Command):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: int
