from src.common.commands import Command


class CreateAccessTokenCommand(Command):
    username: str
    password: str
