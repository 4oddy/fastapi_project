from src.common.exceptions.base_error import BaseError


class UserDoesNotExistError(BaseError):
    message = 'User does not exist.'


class UserAlreadyExistsError(BaseError):
    message = 'User already exists.'
