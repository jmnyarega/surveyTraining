from flask_restplus import Api, Resource, fields
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
login_test = api.model('Login', {
    'username': fields.String,
    'description': fields.String,
})
# ---------------------------------

parser = api.parser()
parser.add_argument('task', type=str, required=True,
                    help='The task details', location='form')

_users = api.namespace('Users', description="Managing users")


@api.errorhandler
def handle_custom_exception(error):
    return {'message': str(error)}, 401


@api.errorhandler
def handle_custom_exception(error):
    return {'message': str(error)}, 500


@_users.route('/api/v1/auth/login', strict_slashes=False)
class Generate(Resource):
    @api.expect(login_test)
    def post(self):
        """ A router to login in the user """
        pass
