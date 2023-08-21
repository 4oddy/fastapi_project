from src.common.services import generate_uuid

from ..entities.user import User


class UserService:
    def create_user(
            self, username: str, first_name: str,
            last_name: str, age: int
    ) -> User:
        return User(
            id=generate_uuid(),
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age
        )
