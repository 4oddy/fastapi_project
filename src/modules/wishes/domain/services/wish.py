from src.common.services import generate_uuid
from src.modules.users.domain.entities.user import User

from ..entities.wish import Wish


class WishService:
    def create_wish(
            self, title: str, description: str, owner: User
    ) -> Wish:
        return Wish(
            id=generate_uuid(),
            title=title,
            description=description,
            owner=owner
        )
