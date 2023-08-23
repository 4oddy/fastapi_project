from src.common.use_case import UseCase

from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork
from .dto import DeleteUserByIdCommand


class DeleteUserByIdUseCase(UseCase[DeleteUserByIdCommand, str]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, data: DeleteUserByIdCommand) -> str:
        result = self.unit_of_work.repository.delete_by_id(data.user_id)
        self.unit_of_work.commit()
        return result
