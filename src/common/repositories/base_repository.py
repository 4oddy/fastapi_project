from typing import Generic, TypeVar, Sequence

from sqlalchemy.orm import Session

_T = TypeVar('_T')


class BaseRepository(Generic[_T]):
    """
        Abstract generic Repository
    """

    def __init__(self, session: Session):
        self.session = session

    def create(self, entity: _T) -> _T:
        raise NotImplementedError

    def findall(self) -> Sequence[_T]:
        raise NotImplementedError

    def find_by_id(self, id_: str) -> _T | None:
        raise NotImplementedError

    def update(self, entity: _T) -> _T:
        raise NotImplementedError

    def delete_by_id(self, id_: str) -> _T:
        raise NotImplementedError
