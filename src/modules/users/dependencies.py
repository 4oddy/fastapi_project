from fastapi import Depends

from sqlalchemy.orm import Session

from src.common.infrastructure.database import get_session
from .infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from .infrastructure.repositories.user_unit_of_work_impl import UserUnitOfWorkImpl
from .application.create_user.use_case import CreateUserUseCase
from .application.list_users.use_case import ListUsersUseCase
from .application.find_by_username.use_case import FindByUsernameUseCase


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
