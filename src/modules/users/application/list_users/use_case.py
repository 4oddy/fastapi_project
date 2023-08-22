from typing import Sequence

from src.common.use_case import UseCase

from ...domain.entities.user import User
from ...infrastructure.repositories.user_repository_impl import UserRepositoryImpl


class ListUsersUseCase(UseCase[None, Sequence[User]]):
    def __init__(self, user_repo: UserRepositoryImpl):
        self.user_repo = user_repo

    def __call__(self) -> Sequence[User]:
        return self.user_repo.findall()
