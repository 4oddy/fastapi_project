from typing import TypeVar, Sequence, Generic

_T = TypeVar('_T')


class BaseRepository(Generic[_T]):
    """
        Abstract generic Repository
    """

    def create(self, entity: _T) -> _T:
        raise NotImplementedError

    def findall(self) -> Sequence[_T]:
        raise NotImplementedError

    def find_by_id(self, id_: int) -> _T | None:
        raise NotImplementedError

    def update(self, entity: _T) -> _T:
        raise NotImplementedError

    def delete_by_id(self, id_: int) -> _T:
        raise NotImplementedError
