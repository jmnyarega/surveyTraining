from flask import jsonify, request, json, make_response
from flask_restplus import Api, Resource, fields
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from flask_jwt import JWT, jwt_required, current_identity

from app import app
from app.models.user import User

user = User()
# setting up authorization headers
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# initializing the api variable
api = Api(app, version='1.0', title='Training Api',
          description='Training Api',
          authorizations=authorizations,
          security='apikey'
          )


# create form-fields for swagger api
# ---------------------------------

events = api.model('Events', {
    'name': fields.String,
    'description': fields.String,
})

sessions = api.model('Sessions', {
    'user_id': fields.String,
    'event_id': fields.String,
})

login_test = api.model('Login', {
    'username': fields.String,
    'description': fields.String,
})
# ---------------------------------


def verify(username, password):
    ''' Verify username and password '''
    if not (username and password):
        return "invalid token"
    u = user.authenticate(username)
    if u:
        if u.password == password:
            return u
    else:
        return False


def identity(payload):
    print(payload)
    ''' Getting user_id from payload to identify the current user '''
    user_id = payload['identity']
    return user_id


# initializing jwt variable
jwt = JWT(app, verify, identity)

parser = api.parser()
parser.add_argument('task', type=str, required=True,
                    help='The task details', location='form')


@api.errorhandler
def handle_custom_exception(error):
    return {'message': str(error)}, 401

@api.errorhandler
def handle_custom_exception(error):
    return {'message': str(error)}, 500


@api.route('/api/v1/auth/login', strict_slashes=False)
class Generate(Resource):
    @api.expect(login_test)
    def post(self):
        ''' A router to login in the user '''
        pass
