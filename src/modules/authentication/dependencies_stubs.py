from .application.create_access_token.use_case import CreateAccessTokenUseCase
from .services.authentication_service import AuthenticationService


def get_authentication_service_stub() -> AuthenticationService:
    ...


def get_create_access_token_use_case_stub() -> CreateAccessTokenUseCase:
    ...
