from flask_restplus import Resource
from flask import request, make_response, jsonify

from .main import api, sessions, parser
from .models.session import Session

session = Session()
_session = api.namespace('Sessions', description="Managing Session")

@_session.route('/api/v1/sessions/', strict_slashes=False,
           endpoint='sessions', methods=['POST', 'GET', 'PUT'])
@_session.route('/api/v1/sessions/<session_id>', strict_slashes=False,
           endpoint='session', methods=['DELETE', 'GET'])
class EventsResource(Resource):

    def get(self, **kwargs):
        ''' gets data from `sessions` table  '''
        if kwargs.get('session_id') is not None:
            response = session.get_session(
                kwargs['session_id'])
        else:
            response = session.get_session()
        return response

    def delete(self, **kwargs):
        ''' deletes data from `events` table  '''
        response = session.delete_session(kwargs.get('session_id'))
        return response

    @api.expect(sessions)
    @api.doc(parser=parser)
    def post(self, **kwargs):
        ''' adds data to `events` table  '''
        data = request.get_json()
        response = session.add_session(data)
        return response
