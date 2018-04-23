from flask_restplus import Resource, fields
from flask import request

from .models.helpers import Helpers
from .main import api, parser
from .models.roles import Role
from app import db

_role = api.namespace('roles', description="Managing user Roles")
helper = Helpers()

roles_marshal = api.model('Roles', {
    'id': fields.Integer,
    'name': fields.String,
    'created_at': fields.String,
})


@_role.route('/api/v1/roles/', strict_slashes=False,
                endpoint='roles', methods=['POST', 'GET', 'PUT'])
@_role.route('/api/v1/roles/<int:role_id>', strict_slashes=False,
                endpoint='role', methods=['DELETE', 'GET'])
class RolesResource(Resource):

    def get(self, **kwargs):
        """ gets role(s) from `roles` table  """
        try:
            role_id = kwargs.get('role_id')
            role_obj = Role.query.all()
            if role_id:
                role_obj = Role.query.filter_by(id=role_id).first()

            if role_obj:
                return helper.handle_200_success(
                    helper.serialize([role_obj], roles_marshal)
                )
            else:
                return helper.handle_404_success([])
        except Exception as e:
            return helper.handle_400_bad_request(e)

    def delete(self, **kwargs):
        """ deletes data from `events` table  """
        role_id = kwargs.get ('role_id')
        try:
            role = Role.query.filter_by(id=role_id).first()
            db.session.delete(role)
            db.session.commit()
            return helper.handle_204_delete_success('Successfully deleted')
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    @api.expect(roles_marshal)
    @api.doc(parser=parser)
    def post(self):
        """ adds a role to `roles` table  """
        try:
            data = request.get_json()
            role = Role(
                name=data.get('name'),
            )
            db.session.add(role)
            db.session.commit()
            return helper.handle_201_success(data)
        except Exception as e:
            return helper.handle_400_bad_request(str(e))
