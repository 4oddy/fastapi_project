from fastapi import Depends

from sqlalchemy.orm import Session

from src.common.infrastructure.database import get_session
from .infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from .infrastructure.repositories.user_unit_of_work_impl import UserUnitOfWorkImpl
from .application.create_user.use_case import CreateUserUseCase


def get_user_repository(session: Session = Depends(get_session)) -> UserRepositoryImpl:
    return UserRepositoryImpl(session)


def get_user_unit_of_work(
        session: Session = Depends(get_session),
        repo: UserRepositoryImpl = Depends(get_user_repository)
) -> UserUnitOfWorkImpl:
    return UserUnitOfWorkImpl(session, repo)


def get_create_user_usecase(uow: UserUnitOfWorkImpl = Depends(get_user_unit_of_work)) -> CreateUserUseCase:
    return CreateUserUseCase(uow)
