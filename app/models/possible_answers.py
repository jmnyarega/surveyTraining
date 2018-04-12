import datetime

from sqlalchemy.sql import func

from app import db


class PossibleAnswers(db.Model):
    '''
    Defines properties for possible answers to generate possible answers
    table in the database
    '''
    __tablename__ = 'possible_answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'),
                            nullable=False)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)

    def __init__(
        self,
        question_id,
        name
    ):
        self.question_id = question_id
        self.name = name

    def __str__(self):
        return "QuestionGroup(id='%s')" % self.id
