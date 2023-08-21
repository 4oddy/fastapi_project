from src.common.repositories.base_repository import BaseRepository

from src.modules.wishes.domain.entities.wish import Wish


class WishRepository(BaseRepository[Wish]):
    ...
