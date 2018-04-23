from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

from instance.config import app_config

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()


def create_app(config_name):
    app.config.from_object(app_config[config_name])  # Configure app according to the environment
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


create_app('development')

from .models.user import User
from .models.events import Events
from .models.session import Session
from .models.questions import Question
from .models.questionGroup import QuestionGroup
from .models.user_answers import UserAnswers
from .models.possible_answers import PossibleAnswers
from .models.roles import Role
