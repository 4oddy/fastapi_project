from src.common.use_case import UseCase

from .dto import CreateAccessTokenCommand


class CreateAccessTokenUseCase(UseCase[CreateAccessTokenCommand, str]):
    def __init__(self):
        ...

    def __call__(self, *args, **kwargs):
        ...
