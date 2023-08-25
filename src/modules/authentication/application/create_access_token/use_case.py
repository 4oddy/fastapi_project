from src.common.use_case import UseCase
from src.modules.authentication.services.authentication_service import \
    AuthenticationService

from .dto import CreateAccessTokenCommand


class CreateAccessTokenUseCase(UseCase[CreateAccessTokenCommand, str]):
    def __init__(self, authentication_service: AuthenticationService):
        self.authentication_service = authentication_service


class CreateAccessTokenUseCaseImpl(CreateAccessTokenUseCase):
    def __call__(self, data: CreateAccessTokenCommand) -> str:
        user = self.authentication_service.authenticate_user(
            data.username, data.password
        )

        token = self.authentication_service.create_access_token(
            {'sub': user.username}
        )

        return token
