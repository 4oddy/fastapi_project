from src.common.use_case import UseCase

from ...domain.entities.user import User
from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork
from .dto import CreateUserCommand

from ..services import get_hashed_password


class CreateUserUseCase(UseCase[CreateUserCommand, str]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, data: CreateUserCommand) -> str:
        hashed_password = get_hashed_password(data.password)

        user = User.create_user(
            username=data.username,
            password=hashed_password,
            first_name=data.first_name,
            last_name=data.last_name,
            age=data.age
        )

        self.unit_of_work.repository.create(user)
        self.unit_of_work.commit()

        return user.id
