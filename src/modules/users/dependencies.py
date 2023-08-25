from fastapi import Depends
from sqlalchemy.orm import Session

from src.common.infrastructure.database import get_session
from src.modules.users.application.create_user.use_case import \
    CreateUserUseCaseImpl
from src.modules.users.application.delete_by_id.use_case import \
    DeleteUserByIdUseCaseImpl
from src.modules.users.application.find_by_username.use_case import \
    FindByUsernameUseCaseImpl
from src.modules.users.application.list_users.use_case import \
    ListUsersUseCaseImpl
from src.modules.users.application.update_user.use_case import \
    UpdateUserUseCaseImpl
from src.modules.users.infrastructure.repositories.user_repository_impl import \
    UserRepositoryImpl
from src.modules.users.infrastructure.repositories.user_unit_of_work_impl import \
    UserUnitOfWorkImpl


def get_user_repository(session: Session = Depends(get_session)) -> UserRepositoryImpl:
    return UserRepositoryImpl(session)


def get_user_unit_of_work(
        session: Session = Depends(get_session),
        repo: UserRepositoryImpl = Depends(get_user_repository)
) -> UserUnitOfWorkImpl:
    return UserUnitOfWorkImpl(session, repo)


def get_create_user_use_case(
        uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)
) -> CreateUserUseCaseImpl:
    return CreateUserUseCaseImpl(uow)


def get_list_users_use_case(
        repo: UserRepositoryImpl = Depends(get_user_repository)
) -> ListUsersUseCaseImpl:
    return ListUsersUseCaseImpl(repo)


def get_find_by_username_use_case(
        repo: UserRepositoryImpl = Depends(get_user_repository)
) -> FindByUsernameUseCaseImpl:
    return FindByUsernameUseCaseImpl(repo)


def get_delete_by_id_use_case(
        uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)
) -> DeleteUserByIdUseCaseImpl:
    return DeleteUserByIdUseCaseImpl(uow)


def get_update_user_use_case(
        uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)
) -> UpdateUserUseCaseImpl:
    return UpdateUserUseCaseImpl(uow)
