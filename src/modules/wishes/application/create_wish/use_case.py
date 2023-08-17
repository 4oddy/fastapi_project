from common.use_case import UseCase

from ...domain.services.wish import WishService
from .dto import CreateWishCommand


class CreateWishUseCase(UseCase[CreateWishCommand, str]):
    def __init__(
            self,
            db_gateway: ...,
            wish_service: WishService
    ):
        self.db_gateway = db_gateway
        self.wish_service = wish_service

    def __call__(self, data: CreateWishCommand) -> str:
        owner = self.db_gateway.get_user(user_id=data.user_id)

        wish = self.wish_service.create_wish(
            title=data.title,
            description=data.description,
            owner=owner
        )

        self.db_gateway.save_wish(wish)
        self.db_gateway.commit()

        return wish.id
