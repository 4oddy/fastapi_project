from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from .base_repository import BaseRepository

_T = TypeVar('_T')


class BaseUnitOfWork(Generic[_T]):

    repository: _T

    def __init__(self, session: Session, repository: BaseRepository):
        self.session = session
        self.repository = repository

    def begin(self):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError
