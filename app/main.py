from flask_restplus import Api, Resource, fields
from app import app

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


parser = api.parser()
parser.add_argument('task', type=str, required=True,
                    help='The task details', location='Nairobi')
