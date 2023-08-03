from common.interfaces import (
    Commiter, WishSaver, UserReader
)


class DbGateway(
    Commiter, WishSaver, UserReader
):
    ...
