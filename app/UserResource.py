from flask_restplus import Resource, fields
from flask import request, make_response, jsonify

from .main import api, parser
from .models.user import User
from .models.helpers import Helpers
from app import db

_session = api.namespace('User', description="Managing User")
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
    'start_date': fields.Date,
    'created_at': fields.Date,
})


@_session.route('/api/v1/users/', strict_slashes=False,
                endpoint='users', methods=['POST', 'GET', 'PUT'])
@_session.route('/api/v1/sessions/<user_id>', strict_slashes=False,
                endpoint='user', methods=['DELETE', 'GET'])
class UserResource(Resource):

    def get(self, **kwargs):
        """ gets data from `sessions` table  """
        user_id = kwargs.get('user_id')
        user_obj = User.query.all()
        if kwargs.get('user_id'):
            user_obj = [User.query.filter_by(id=user_id).first()]

        if user_obj:
            return helper.handle_200_success(
                helper.serialize(user_obj, 'data', user_marshal)
            )
        else:
            return helper.handle_404_success([])

    def delete(self, **kwargs):
        """ deletes data from `events` table  """
        try:
            user = User.query.filter_by(id=kwargs.get('user_id')).first()
            db.session.delete(user)
            db.session.commit()
            return helper.handle_204_delete_success('User deleted successfully')
        except Exception as e:
            return helper.handle_400_bad_request('Error in deleting user')

    @api.expect(user_marshal)
    @api.doc(parser=parser)
    def post(self):
        """ adds data to `events` table  """
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
            return helper.handle_400_bad_request('Error in adding session')
