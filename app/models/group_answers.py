import datetime

from sqlalchemy.sql import func

from app import db


class GroupAnswers(db.Model):
    '''
    Defines properties for question group answer to generate group answers
    table in the database
    '''
    __tablename__ = 'group_answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_group_id = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime,
                           server_default=func.now(), nullable=False)

    def __init__(
        self,
        question_group_id,
        answer
    ):
        self.question_group_id = question_group_id
        self.answer = answer

    def __str__(self):
        return "GroupAnswers(id='%s')" % self.id
