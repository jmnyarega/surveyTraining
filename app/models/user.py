from sqlalchemy.sql import func

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app import db


class User(db.Model):
    """
    Defines properties for a user to generate users table in db
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(120), unique=True)
    mobile = Column(String(120), unique=True)
    gender = Column(String(10), nullable=False)
    profession = Column(String(10), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(DateTime(), server_default=func.now(), nullable=False)

    def __init__(
        self,
        firstname='',
        lastname='',
        email='',
        mobile='',
        gender='',
        profession=''
    ):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobile = mobile
        self.gender = gender
        self.profession = profession

    def __str__(self):
        return "User(id='%s')" % self.id

    def authenticate(self, username):
        print(username)
