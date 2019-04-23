# coding=utf-8

from sqlalchemy import Column, String, Integer
from werkzeug.security import check_password_hash

from dao.base import Base, Session


class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    name = Column(String(50))
    user = Column(String(20), unique=True)
    password = Column(String(100))
    status = Column(Integer)

    def __init__(self, user=None, password=None, name=None, created_when=None,
                 status=None):

        self.name = name
        self.user = user
        self.created_when = created_when
        self.password = password
        self.status = status

    def verify_user(self):

        session = Session()
        isvalid = session.query(User) \
            .filter(User.user == self.user) \
            .all()
        session.close()
        if len(isvalid) > 0 and isvalid[0].status == 1:
            passw1 = isvalid[0].password

            if check_password_hash(passw1, self.password):
                return True
        return False
