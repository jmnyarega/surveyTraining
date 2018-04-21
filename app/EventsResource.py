from flask_restplus import Resource, marshal, fields
from flask import request

from .main import api, parser
from app import db
from .models.helpers import Helpers
from .models.events import Events

event = Events()
helper = Helpers()
_events = api.namespace('events', description="Managing Events")

events_marshal = api.model('Events', {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'start_date': fields.Date,
    'end_date': fields.Date,
    'token': fields.String,
    'user_id': fields.String,
    'created_at': fields.String,
})


@_events.route('/api/v1/events/', strict_slashes=False,
               endpoint='events', methods=['POST', 'GET', 'PUT'])
@_events.route('/api/v1/events/<int:event_id>', strict_slashes=False,
               endpoint='event', methods=['DELETE', 'GET'])
class EventsResource(Resource):

    def get(self, **kwargs):
        """ gets event(s) from `events` table  """
        try:
            event_id = kwargs.get('event_id')
            event_obj = Events.query.all()
            if event_id:
                event_obj = Events.query.filter_by(id=event_id).first()

            if event_obj:
                return helper.handle_200_success(
                    helper.serialize([event_obj], 'data', events_marshal)
                )
            else:
                return helper.handle_404_success([])
        except Exception as e:
            return helper.handle_500_error(str(e))

    def delete(self, event_id):
        """ deletes data from `events` table  """
        try:
            event_obj = Events.query.filter_by(id=event_id).first()
            db.session.delete(event_obj)
            db.session.commit()
            return helper.handle_204_delete_success('Event Successfully deleted')
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    @api.expect(events_marshal)
    @api.doc(parser=parser)
    def put(self):
        """ updates event => `events` table  """
        data = request.get_json()
        try:
            event_obj = Events.query.filter_by(id=data.get('id')).first()
            event_obj.name = data.get('name')
            event_obj.description = data.get('description')
            if data.get('start_date'):
                event_obj.start_date = data.get('start_date')
            if data.get('start_date'):
                event_obj.end_date = data.get('end_date')
            db.session.add(event_obj)
            db.session.commit()
            return helper.handle_201_success([data])
        except Exception as e:
            return helper.handle_400_bad_request(str(e))

    @api.expect(events_marshal)
    @api.doc(parser=parser)
    def post(self):
        """ adds new event to `events` table  """
        data = request.get_json()
        try:
            event_obj = Events(
                name=data.get('name'),
                description=data.get('description')
            )
            db.session.add(event_obj)
            db.session.commit()
            return helper.handle_201_success(data)
        except Exception as e:
            return helper.handle_400_bad_request(str(e))
