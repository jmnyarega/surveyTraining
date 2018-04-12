from flask import jsonify, request, json, make_response
from flask_restplus import Api, Resource, fields
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from flask_jwt import JWT, jwt_required, current_identity

from app import app
from app.models.events import Events

event = Events()

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

event = api.model('Events', {
    'name': fields.String,
    'description': fields.String,
})

# ---------------------------------


def verify(username, password):
    ''' Verify username and password '''
    if not (username and password):
        return "invalid token"
    u = user.authenticate(username)
    if u:
        if check_password_hash(u.password, password):
            return u
    else:
        return False


def identity(payload):
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


@api.route('/events/', strict_slashes=False,
           endpoint='events', methods=['POST', 'GET'])
class Event(Resource):

    def get(self, **kwargs):
        ''' gets data from `events` table  '''
        if kwargs.get("event_id") is not None:
            response = event.get_events(
                kwargs['event_id'])
        else:
            response = event.get_events()
        return response

    @jwt_required()
    def delete(self, **kwargs):
        ''' deletes data from `events` table  '''
        response = event.delete_event(kwargs['event_id'])
        return response

    @api.expect(event)
    @api.doc(parser=parser)
    @jwt_required()
    def put(self, event_id):
        ''' updates data from `events` table  '''
        data = request.get_json()
        response = event.update_event(data)
        return response

    @api.expect(event)
    @api.doc(parser=parser)
    def post(self, **kwargs):
        ''' adds data to `events` table  '''
        data = request.get_json()
        response = event.add_event(data)
        return response


@api.route('/auth/login', strict_slashes=False)
class Generate(Resource):
    @api.expect(login_test)
    def post(self):
        ''' A router to login in the user '''
        pass
