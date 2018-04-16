import datetime

from sqlalchemy.sql import func

from app import db

# helpers
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
        return "Session(id='%s')" % self.id

    def get_session(self, *args):
        sessions = Session.query.first()
        if len(args) > 0:
            sessions = Session.query.filter_by(id=args[0])
        return helper.unpack_query_session_object(sessions)

    def add_session(self, data):
        session = Session(
            event_id=data.get('event_id'),
            user_id=data.get('user_id')
        )
        db.session.add(session)
        db.session.commit()
        print(session)

    def delete_session(self, session_id):
        session = Session.query.filter_by(id=session_id).first()
        db.session.delete(session)
        db.session.commit()
