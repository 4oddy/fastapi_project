from common.services import generate_id

from ..entities.wish import Wish
from modules.users.domain.entities.user import User


class WishService:
    def create_wish(
            self, title: str, description: str, owner: User
    ) -> Wish:
        return Wish(
            id=generate_id(),
            title=title,
            description=description,
            owner=owner
        )
