from .application.create_user.use_case import CreateUserUseCase
from .application.delete_by_id.use_case import DeleteUserByIdUseCase
from .application.find_by_username.use_case import FindByUsernameUseCase
from .application.list_users.use_case import ListUsersUseCase
from .application.update_user.use_case import UpdateUserUseCaseImpl
from .infrastructure.repositories.user_repository import UserRepository
from .infrastructure.repositories.user_unit_of_work import UserUnitOfWork


def get_user_repository_stub() -> UserRepository:
    ...


def get_user_unit_of_work_stub() -> UserUnitOfWork:
    ...


def get_create_user_use_case_stub() -> CreateUserUseCase:
    ...


def get_list_users_use_case_stub() -> ListUsersUseCase:
    ...


def get_find_by_username_use_case_stub() -> FindByUsernameUseCase:
    ...


def get_delete_by_id_use_case_stub() -> DeleteUserByIdUseCase:
    ...


def get_update_user_use_case_stub() -> UpdateUserUseCaseImpl:
    ...
