from typing import Protocol

from modules.wishes.domain.entities.wish import Wish
from modules.users.domain.entities.user import User


class Commiter(Protocol):
    def commit(self) -> None:
        ...


class WishReader(Protocol):
    def get_wish(self, wish_id: str) -> Wish:
        raise NotImplementedError


class WishSaver(Protocol):
    def save_wish(self, data: Wish) -> str:
        raise NotImplementedError


class UserReader(Protocol):
    def get_user(self, user_id: str) -> User:
        raise NotImplementedError


class UserSaver(Protocol):
    def save_user(self, data: User) -> str:
        raise NotImplementedError
