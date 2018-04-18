from sqlalchemy.sql import func

from app import db
from .helpers import Helpers

helper = Helpers()


class Role(db.Model):
    """
    Defines properties for an event to generate an event table in the database
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=func.now())

    def __init__(
        self,
        name='',
        created_at=func.now(),
    ):
        self.name = name
        self.created_at = created_at

    def __str__(self):
        return self.name
