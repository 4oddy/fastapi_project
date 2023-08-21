from src.common.commands import Command


class CreateWishCommand(Command):
    title: str
    description: str
    user_id: int
