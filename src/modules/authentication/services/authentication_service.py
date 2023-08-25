import copy
from datetime import datetime, timedelta

import jwt

from src.common.dependencies import get_settings
from src.modules.authentication.services.password import check_password
from src.modules.users.domain.entities.user import User
from src.modules.users.infrastructure.repositories.user_repository import \
    UserRepository

from ..exceptions.authentication_errors import (InvalidAccessTokenError,
                                                InvalidCredentialsError)

settings = get_settings()


class AuthenticationService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def authenticate_user(self, username: str, plain_password: str) -> User:
        raise NotImplementedError

    @staticmethod
    def create_access_token(
            data: dict,
            expires_delta: timedelta = settings.expires_delta_access_token,
    ) -> str:
        raise NotImplementedError

    def get_user_from_access_token(self, token: str) -> User:
        raise NotImplementedError


class AuthenticationServiceImpl(AuthenticationService):
    def authenticate_user(self, username: str, plain_password: str) -> User:
        user = self.repo.find_by_username(username)

        if user is not None:
            if check_password(plain_password, user.password):
                return user

        raise InvalidCredentialsError()

    @staticmethod
    def create_access_token(
            data: dict,
            expires_delta: timedelta = settings.expires_delta_access_token,
    ) -> str:
        to_encode = copy.deepcopy(data)
        expires = datetime.utcnow() + expires_delta
        to_encode['exp'] = expires

        encoded_jwt = jwt.encode(
            to_encode,
            settings.secret_key,
            'HS256'
        )
        return encoded_jwt

    def get_user_from_access_token(self, token: str) -> User:
        payload: dict = jwt.decode(
            token,
            settings.secret_key,
            algorithms=['HS256']
        )

        username = payload.get('sub', None)

        if username:
            user = self.repo.find_by_username(username)

            if user:
                return user

        raise InvalidAccessTokenError()
