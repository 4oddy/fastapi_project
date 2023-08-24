from src.common.use_case import UseCase

from ...domain.entities.user import User, UserReadModel
from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork
from .dto import UpdateUserCommand

from ...exceptions.user_errors import UserDoesNotExistError


class UpdateUserUseCase(UseCase[tuple[str, UpdateUserCommand], UserReadModel]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, data: tuple[str, UpdateUserCommand]) -> UserReadModel:
        user_id, data = data

        existing_user = self.unit_of_work.repository.find_by_id(user_id)

        if not existing_user:
            raise UserDoesNotExistError()

        user = User(
            id=user_id,
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
            age=data.age,
            password=''
        )

        user = self.unit_of_work.repository.update(user)
        self.unit_of_work.commit()
        return user.to_read_model()
