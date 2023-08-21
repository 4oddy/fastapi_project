from src.common.repositories.base_repository import BaseRepository

from src.modules.users.domain.entities.user import User


class UserRepository(BaseRepository[User]):
    ...
