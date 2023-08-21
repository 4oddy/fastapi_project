from src.common.use_case import UseCase

from ...domain.services.user import UserService
from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork
from .dto import CreateUserCommand


class CreateUserUseCase(UseCase[CreateUserCommand, str]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work
        self.user_service = UserService()

    def __call__(self, data: CreateUserCommand) -> str:
        user = self.user_service.create_user(
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
            age=data.age
        )

        self.unit_of_work.repository.create(user)
        self.unit_of_work.commit()

        return user.id
