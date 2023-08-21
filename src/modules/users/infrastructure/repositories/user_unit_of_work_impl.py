from .user_unit_of_work import UserUnitOfWork


class UserUnitOfWorkImpl(UserUnitOfWork):
    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
