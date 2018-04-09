import unittest
from passlib.hash import bcrypt

from app import app
from app.models.models import db
from app.models.user_controller import UserStore
from app.models.bucket_controller import BucketStore
from app.models.items_controller import ItemStore


class BaseTest(unittest.TestCase):
    def setUp(self):
        #setup test environment configuration
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

        self.headers = {"Content-Type": "application/json"}
        #define a user to be used for registration tests
        self.temp_user = {
            "username": "Sansa",
            "email": "sansa@gmail.com",
            "password": "wicked",
            "confirm_password": "wicked"
        }

        #define an existing user
        self.saved_user = User("tyrion", "tyrion@gmail.com",
                               bcrypt.hash("lion", rounds=12))
        db.session.add(self.saved_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove
        db.drop_all()
