from common.use_case import UseCase

from .dto import CreateUserCommand
from ...domain.services.user import UserService


class CreateUserUseCase(UseCase[CreateUserCommand, str]):
    def __init__(
            self,
            db_gateway: ...,
            user_service: UserService
    ):
        self.db_gateway = db_gateway
        self.user_service = user_service

    def __call__(self, data: CreateUserCommand) -> str:
        user = self.user_service.create_user(
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
            age=data.age
        )

        self.db_gateway.save_user(user)
        self.db_gateway.commit()

        return user.id
