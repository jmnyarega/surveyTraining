from flask_restplus import Resource, fields
from flask import request, make_response, jsonify

from .main import api, parser
from .models.session import Session
from .models.helpers import Helpers
from app import db

_session = api.namespace('Sessions', description="Managing Session")
helper = Helpers()

sessions_marshal = api.model('Sessions', {
    'id': fields.Integer,
    'event_id': fields.Integer,
    'user_id': fields.Integer,
    'start_date': fields.Date,
    'created_at': fields.Date,
})

@_session.route('/api/v1/sessions/', strict_slashes=False,
                endpoint='sessions', methods=['POST', 'GET', 'PUT'])
@_session.route('/api/v1/sessions/<int:session_id>', strict_slashes=False,
                endpoint='session', methods=['DELETE', 'GET'])
class SessionResource(Resource):

    def get(self, **kwargs):
        """ gets session(s) from `sessions` table  """
        try:
            session_id = kwargs.get('session_id')
            session_obj = Session.query.all()
            if session_id:
                session_obj = Session.query.filter_by(id=session_id).first()
            if session_obj:
                return helper.handle_200_success(
                    helper.serialize([session_obj], sessions_marshal)
                )
            else:
                return helper.handle_404_success([])
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    def delete(self, **kwargs):
        """ deletes data from `session` table  """
        session_id = kwargs.get ('session_id')
        try:
            session = Session.query.filter_by(id=session_id).first()
            db.session.delete(session)
            db.session.commit()
            return helper.handle_204_delete_success('Session deleted successfully')
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    @api.expect(sessions_marshal)
    @api.doc(parser=parser)
    def post(self):
        """ adds data to `session` table  """
        try:
            data = request.get_json()
            session = Session(
                event_id=data.get('event_id'),
                user_id=data.get('user_id')
            )
            db.session.add(session)
            db.session.commit()
            return helper.handle_201_success('Session successfully created')
        except Exception as e:
            return helper.handle_400_bad_request(str(e))
