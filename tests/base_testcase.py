import unittest

from app import app, db
from app.models.user import User
from app.models.events import Events
from app.models.session import Session
from app.models.questions import Question
from app.models.questionGroup import QuestionGroup
from app.models.group_answers import GroupAnswers
from app.models.answers import Answers


class BaseTest(unittest.TestCase):
    def setUp(self):
        # setup test environment configuration
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_test.db'
        self.app = app.test_client()
        db.create_all()

        self.headers = {"Content-Type": "application/json"}
        # define a user to be used for registration tests
        self.temp_user = {
            "firstname": "Sansa",
            "email": "sansa@gmail.com",
            "lastname": "Doe",
            "gender": "F",
            "profession": "IT",
        }

        # define an existing user
        self.saved_user = User("firstname", "lastname",
                               "email", "mobile", "gender", "profession")
        db.session.add(self.saved_user)
        db.session.commit()

    def test_testing(self):
        self.assertEquals(1, 7)

    def tearDown(self):
        db.session.remove
        db.drop_all()
