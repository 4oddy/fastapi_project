from fastapi import Depends

from src.modules.users.dependencies import get_user_repository, UserRepositoryImpl
from .services.authentication_service import AuthenticationService


def get_authentication_service(repo: UserRepositoryImpl = Depends(get_user_repository)) -> AuthenticationService:
    return AuthenticationService(repo)
