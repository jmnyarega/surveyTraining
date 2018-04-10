import datetime

from sqlalchemy.sql import func

from app import db


class Answers(db.Model):
    '''
    Defines properties for answer to generate answers table in the database
    '''
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    answer = db.Column(db.String(80), nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)

    def __init__(
        self,
        user_id,
        session_id,
        question_id,
        answer
    ):
        self.user_id = user_id
        self.session_id = session_id
        self.question_id = question_id
        self.answer = answer

    def __str__(self):
        return "Answers(id='%s')" % self.id
