from src.common.use_case import UseCase

from .dto import FindByUsernameQuery
from ...domain.entities.user import User
from ...infrastructure.repositories.user_repository import UserRepository


class FindByUsernameUseCase(UseCase[FindByUsernameQuery, User]):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def __call__(self, data: FindByUsernameQuery) -> User:
        user = self.repo.find_by_username(data.username)
        return user
