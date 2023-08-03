from common.interfaces import UserSaver, Commiter


class DbGateway(UserSaver, Commiter):
    ...
