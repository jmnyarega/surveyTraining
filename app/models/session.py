from sqlalchemy.sql import func

from app import db
from .helpers import Helpers

helper = Helpers()


class Session(db.Model):
    """
    Defines properties for an event to generate an event table in the database
    """
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    start_date = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)

    def __init__(
        self,
        event_id='',
        user_id='',
        start_date=func.now(),
    ):
        self.event_id = event_id
        self.user_id = user_id
        self.start_date = start_date

    def __str__(self):
        return self.id
