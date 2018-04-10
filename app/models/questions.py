import datetime

from sqlalchemy.sql import func

from app import db


class Question(db.Model):
    '''
    Defines properties for question to generate questions table in the database
    '''
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(80), nullable=False)
    question_type = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)

    def __init__(
        self,
        question,
        question_type,
        user_id,
    ):
        self.question = question
        self.user_id = user_id
        self.question_type = question_type

    def __str__(self):
        return "Question(id='%s')" % self.id
