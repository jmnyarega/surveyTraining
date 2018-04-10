from sqlalchemy.sql import func

from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from app import db


class Events(db.Model):
    '''
    Defines properties for an event to generate an event table in the database
    '''
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    description = Column(String(80), nullable=False)
    start_date = Column(DateTime(), server_default=func.now())
    end_date = Column(DateTime(), server_default=func.now())
    token = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(
        self,
        name,
        description,
        start_date,
        end_date,
        token
    ):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.token = token

    def __str__(self):
        return "Event(id='%s')" % self.id
