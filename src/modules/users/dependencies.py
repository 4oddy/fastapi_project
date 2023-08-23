from fastapi import Depends
from sqlalchemy.orm import Session

from src.common.infrastructure.database import get_session

from .application.create_user.use_case import CreateUserUseCase
from .application.delete_by_id.use_case import DeleteUserByIdUseCase
from .application.find_by_username.use_case import FindByUsernameUseCase
from .application.list_users.use_case import ListUsersUseCase
from .application.update_user.use_case import UpdateUserUseCase
from .infrastructure.repositories.user_repository_impl import \
    UserRepositoryImpl
from .infrastructure.repositories.user_unit_of_work_impl import \
    UserUnitOfWorkImpl


def get_user_repository(session: Session = Depends(get_session)) -> UserRepositoryImpl:
    return UserRepositoryImpl(session)


def get_user_unit_of_work(
        session: Session = Depends(get_session),
        repo: UserRepositoryImpl = Depends(get_user_repository)
) -> UserUnitOfWorkImpl:
    return UserUnitOfWorkImpl(session, repo)


def get_create_user_use_case(uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)) -> CreateUserUseCase:
    return CreateUserUseCase(uow)


def get_list_users_use_case(repo: UserRepositoryImpl = Depends(get_user_repository)) -> ListUsersUseCase:
    return ListUsersUseCase(repo)


def get_find_by_username_use_case(repo: UserRepositoryImpl = Depends(get_user_repository)) -> FindByUsernameUseCase:
    return FindByUsernameUseCase(repo)


def get_delete_by_id_use_case(uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)) -> DeleteUserByIdUseCase:
    return DeleteUserByIdUseCase(uow)


def get_update_user_use_case(uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)) -> UpdateUserUseCase:
    return UpdateUserUseCase(uow)
