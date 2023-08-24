from src.common.exceptions.base_error import BaseError


class InvalidCredentialsError(BaseError):
    message = 'Incorrect username or password.'


class InvalidAccessTokenError(BaseError):
    message = 'Invalid Access Token.'
