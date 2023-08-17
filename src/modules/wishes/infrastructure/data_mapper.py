from common.infrastructure.data_mapper import BaseDataMapper
from modules.users.domain.entities.user import User

from ..domain.entities.wish import Wish
from ..infrastructure.models import Wish as WishModel


class WishDataMapper(BaseDataMapper):
    def model_to_entity(self, model: WishModel) -> Wish:
        # return Wish(
        #     id=model.id,
        #     title=model.title,
        #     description=model.description,
        #     owner=User(
        #         id=model.owner.id,
        #         username=model.owner.username,
        #         first_name=model.owner.first_name,
        #         last_name=model.owner.last_name,
        #         age=model.owner.age
        #     )
        # )
        ...

    def entity_to_model(self, entity: Wish) -> WishModel:
        ...
