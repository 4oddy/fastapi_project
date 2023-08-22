from typing import Sequence

from src.common.use_case import UseCase

from ...domain.entities.user import User
from ...infrastructure.repositories.user_repository import UserRepository


class ListUsersUseCase(UseCase[None, Sequence[User]]):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def __call__(self) -> Sequence[User]:
        return self.repo.findall()
