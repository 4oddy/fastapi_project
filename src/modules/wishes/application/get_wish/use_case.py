from common.use_case import UseCase

from ...domain.entities.wish import Wish
from ...domain.services.wish import WishService
from .dto import GetWishQuery


class GetWishUseCase(UseCase[GetWishQuery, Wish]):
    def __init__(
            self,
            db_gateway: ...,
            wish_service: WishService
    ):
        self.db_gateway = db_gateway
        self.wish_service = wish_service

    def __call__(self, data: GetWishQuery) -> Wish:
        wish = self.db_gateway.get_wish(data.wish_id)
        return wish
