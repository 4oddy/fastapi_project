from fastapi import Depends

from src.modules.users.dependencies import (UserRepositoryImpl,
                                            get_user_repository)

from .application.create_access_token.use_case import \
    CreateAccessTokenUseCaseImpl
from .services.authentication_service import AuthenticationServiceImpl


def get_authentication_service(
        repo: UserRepositoryImpl = Depends(get_user_repository)
) -> AuthenticationServiceImpl:
    return AuthenticationServiceImpl(repo)


def get_create_access_token_use_case(
        auth_service: AuthenticationServiceImpl = Depends(get_authentication_service)
) -> CreateAccessTokenUseCaseImpl:
    return CreateAccessTokenUseCaseImpl(auth_service)
