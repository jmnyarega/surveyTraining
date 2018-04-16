from flask_restplus import Resource
from flask import request, make_response, jsonify

from .main import api, sessions, parser
from .models.roles import Role

role = Role()
_session = api.namespace('Roles', description="Managing user Roles")


@_session.route('/api/v1/roles/', strict_slashes=False,
                endpoint='roles', methods=['POST', 'GET', 'PUT'])
@_session.route('/api/v1/roles/<role_id>', strict_slashes=False,
                endpoint='role', methods=['DELETE', 'GET'])
class EventsResource(Resource):

    def get(self, **kwargs):
        """ gets data from `sessions` table  """
        if kwargs.get('role_id') is not None:
            response = role.get_role(
                kwargs['role_id'])
        else:
            response = role.get_role()
        return response

    def delete(self, **kwargs):
        """ deletes data from `events` table  """
        response = role.delete_role(kwargs.get('role_id'))
        return response

    @api.expect(sessions)
    @api.doc(parser=parser)
    def post(self):
        """ adds data to `events` table  """
        data = request.get_json()
        response = role.add_role(data)
        return response
