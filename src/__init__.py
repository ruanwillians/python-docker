from .config import DBConection
from .entities.users import Users as UsersModel

class UserRepo:

    def insert_user(self, name):
        with DBConection() as db:
            new_user = UsersModel(name=name)
            db.session.add(new_user)
            db.session.commit()