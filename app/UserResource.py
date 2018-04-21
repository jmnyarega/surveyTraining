from flask_restplus import Resource, fields
from flask import request, make_response, jsonify

from .main import api, parser
from .models.user import User
from .models.helpers import Helpers
from app import db

_users = api.namespace('Users', description="Managing Users")
helper = Helpers()

user_marshal = api.model('User', {
    'id': fields.Integer,
    'firstname': fields.String,
    'lastname': fields.String,
    'email': fields.String,
    'mobile': fields.String,
    'gender': fields.String,
    'profession': fields.String,
    'role_id': fields.Integer,
    'created_at': fields.Date,
})

user_role = api.model('UserRole', {
    'id': fields.Integer,
    'role_id': fields.Integer,
})

@_users.route('/api/v1/users/', strict_slashes=False,
                endpoint='users', methods=['POST', 'GET', 'PUT'])
@_users.route('/api/v1/users/<int:user_id>/<int:role_id>', strict_slashes=False,
                endpoint='user-roles', methods=['DELETE', 'GET'])
@_users.route('/api/v1/users/<int:user_id>', strict_slashes=False,
                endpoint='user', methods=['GET'])
@_users.route('/api/v1/users/<int:role_id>', strict_slashes=False,
                endpoint='role-user', methods=['GET'])
class UserResource(Resource):

    def get(self, **kwargs):
        """ gets user(s) from `users` table  """
        user_id = kwargs.get('user_id')
        role_id = kwargs.get ('role_id')
        user_obj = User.query.all()
        if user_id:
            user_obj = User.query.filter_by(id=user_id).first()
            if role_id:
                user_obj = User.query.filter_by(id=user_id, role_id=role_id).first()
        if role_id and user_id is None:
            user_obj = User.query.filter_by (role_id=role_id).all()

        if user_obj is None :
            return helper.handle_404_success([])
        elif  user_obj:
            return helper.handle_200_success(
                helper.serialize([user_obj], 'data', user_marshal)
            )

    def delete(self, **kwargs):
        """ deletes user from `users` table  """
        try:
            user = User.query.filter_by(id=kwargs.get('user_id'),
                                        role_id=kwargs['role_id']).first()
            db.session.delete(user)
            db.session.commit()
            return helper.handle_204_delete_success('User deleted successfully')
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    @api.expect(user_marshal)
    @api.doc(parser=parser)
    def post(self):
        """ adds a user  """
        try:
            data = request.get_json()
            user = User(
                firstname=data.get('firstname'),
                lastname=data.get ('lastname'),
                email=data.get ('email'),
                profession=data.get('profession'),
                mobile=data.get ('mobile'),
                gender=data.get ('gender'),
                role_id=data.get ('role_id'),
            )
            db.session.add(user)
            db.session.commit()
            return helper.handle_201_success('User successfully created')
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    @api.expect(user_role)
    @api.doc(parser=parser)
    def put(self):
        """ assign role to a user  """
        try:
            data = request.get_json()
            user_id = data.get('user_id')
            role_id = data.get('role_id')
            user = User.query.filter_by(id=user_id).first()
            user.role_id = role_id
            db.session.add(user)
            db.session.commit()
            return helper.handle_201_success ('User successfully assigned a role')
        except Exception as e:
            return helper.handle_400_bad_request(str (e))
