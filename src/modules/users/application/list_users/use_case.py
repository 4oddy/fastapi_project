from typing import Sequence

from src.common.use_case import UseCase

from ...domain.entities.user import UserReadModel
from ...infrastructure.repositories.user_repository import UserRepository


class ListUsersUseCase(UseCase[None, Sequence[UserReadModel]]):
    def __init__(self, repo: UserRepository):
        self.repo = repo


class ListUsersUseCaseImpl(ListUsersUseCase):
    def __call__(self) -> Sequence[UserReadModel]:
        users = self.repo.findall()
        return list(map(lambda user: user.to_read_model(), users))
