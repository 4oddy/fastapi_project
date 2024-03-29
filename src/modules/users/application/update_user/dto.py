from typing import Optional

from src.common.commands import Command


class UpdateUserCommand(Command):
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
