from src.common.repositories.unit_of_work import BaseUnitOfWork

from .user_repository import UserRepository


class UserUnitOfWork(BaseUnitOfWork[UserRepository]):
    ...
