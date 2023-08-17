from .database import Model
from ..entities import Entity


class BaseDataMapper:
    def model_to_entity(self, model: Model) -> Entity:
        raise NotImplementedError

    def entity_to_model(self, entity: Entity) -> Model:
        raise NotImplementedError
