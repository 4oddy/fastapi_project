from dataclasses import dataclass

from common.commands import Command


@dataclass
class CreateWishCommand(Command):
    title: str
    description: str
    user_id: int
