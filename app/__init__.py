from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from .models.user import User
from .models.events import Events
from .models.session import Session
from .models.questions import Question
from .models.questionGroup import QuestionGroup
from .models.user_answers import UserAnswers
from .models.possible_answers import PossibleAnswers
from .models.roles import Role
