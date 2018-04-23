import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from config import app_configuration
from .models.user import User
from .models.events import Events
from .models.session import Session
from .models.questions import Question
from .models.questionGroup import QuestionGroup
from .models.user_answers import UserAnswers
from .models.possible_answers import PossibleAnswers
from .models.roles import Role


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    db.init_app(app)
    return app


app = create_app(app_configuration[os.environ.get('APP_ENV')])
