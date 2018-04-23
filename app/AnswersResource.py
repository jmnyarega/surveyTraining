from flask_restplus import Resource, marshal, fields
from flask import request

from .main import api, parser
from app import db
from .models.helpers import Helpers
from .models.user_answers import UserAnswers

answer = UserAnswers()
helper = Helpers()
_answers = api.namespace('answers', description="Managing Answers")

answers_marshal = api.model('Answers', {
    'id': fields.Integer,
    'user_id': fields.String,
    'session_id': fields.String,
    'question_id': fields.String,
    'answer': fields.String,
    'created_at': fields.Date,
})


@_answers.route('/api/v1/answers/', strict_slashes=False,
               endpoint='answers', methods=['POST', 'GET', 'PUT'])
@_answers.route('/api/v1/answers/<int:user_id>', strict_slashes=False,
               endpoint='answer', methods=['GET'])
class AnswerResource(Resource):

    def get(self, **kwargs):
        """ gets answer(s) from `answers` table  """
        try:
            user_id = kwargs.get('user_id')
            answer_obj = answer.query.all()
            if user_id:
                answer_obj = answer.query.filter_by(id=user_id).first()

            if answer_obj:
                return helper.handle_200_success(
                    helper.serialize([answer_obj], answers_marshal)
                )
            else:
                return helper.handle_404_success([])
        except Exception as e:
            return helper.handle_500_error (str (e))

    @api.expect(answers_marshal)
    @api.doc(parser=parser)
    def post(self):
        """ adds answers to `answers` table  """
        data = request.get_json()
        try:
            answer_obj = UserAnswers(
                user_id=data.get('user_id'),
                session_id=data.get('session_id'),
                question_id=data.get('question_id'),
                answer=data.get('answer')
            )
            db.session.add(answer_obj)
            db.session.commit()
            return helper.handle_201_success(data)
        except Exception as e:
            return helper.handle_400_bad_request(str(e))
