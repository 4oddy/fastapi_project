from src.common.use_case import UseCase

from ...domain.entities.user import UserReadModel
from ...exceptions.user_errors import UserDoesNotExistError
from ...infrastructure.repositories.user_repository import UserRepository
from .dto import FindByUsernameQuery


class FindByUsernameUseCase(UseCase[FindByUsernameQuery, UserReadModel]):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def __call__(self, data: FindByUsernameQuery) -> UserReadModel:
        user = self.repo.find_by_username(data.username)

        if user is None:
            raise UserDoesNotExistError()

        return user.to_read_model()
