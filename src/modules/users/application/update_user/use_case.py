from src.common.use_case import UseCase

from ...domain.entities.user import User, UserReadModel
from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork
from .dto import UpdateUserCommand


class UpdateUserUseCase(UseCase[UpdateUserCommand, UserReadModel]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, data: UpdateUserCommand) -> UserReadModel:
        user = User(
            id=data.id,
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
            age=data.age,
            password=''
        )

        user = self.unit_of_work.repository.update(user)
        self.unit_of_work.commit()
        return user.to_read_model()
