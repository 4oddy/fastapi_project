from src.common.use_case import UseCase

from ...domain.entities.user import User
from ...exceptions.user_errors import UserAlreadyExistsError
from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork
from ..services import get_hashed_password
from .dto import CreateUserCommand


class CreateUserUseCase(UseCase[CreateUserCommand, str]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, data: CreateUserCommand) -> str:
        existing_user = self.unit_of_work.repository.find_by_username(data.username)

        if existing_user:
            raise UserAlreadyExistsError()

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
