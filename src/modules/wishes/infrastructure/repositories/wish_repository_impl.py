from typing import Sequence

from src.modules.wishes.infrastructure.repositories.wish_repository import WishRepository
from ...domain.entities.wish import Wish


class WishRepositoryImpl(WishRepository):
    def create(self, entity: Wish) -> Wish:
        ...

    def findall(self) -> Sequence[Wish]:
        ...

    def find_by_id(self, id_: int) -> Wish | None:
        ...

    def update(self, entity: Wish) -> Wish:
        ...

    def delete_by_id(self, id_: int) -> Wish:
        ...
