from src.common.use_case import UseCase

from ...infrastructure.repositories.user_unit_of_work import UserUnitOfWork


class DeleteUserByIdUseCase(UseCase[str, str]):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, user_id: str) -> str:
        result = self.unit_of_work.repository.delete_by_id(user_id)
        self.unit_of_work.commit()
        return result
