from flask_restplus import Resource
from flask import request

from .main import api, events, parser
from .models.events import Events

event = Events()
_events = api.namespace('events', description="Managing Events")


@_events.route('/api/v1/events/', strict_slashes=False,
               endpoint='events', methods=['POST', 'GET', 'PUT'])
@_events.route('/api/v1/events/<event_id>', strict_slashes=False,
               endpoint='event', methods=['DELETE', 'GET'])
class EventsResource(Resource):

    def get(self, **kwargs):
        """ gets data from `events` table  """
        if kwargs.get("event_id") is not None:
            response = event.get_events(
                kwargs['event_id'])
        else:
            response = event.get_events()
        return response

    def delete(self, **kwargs):
        """ deletes data from `events` table  """
        response = event.delete_event(kwargs['event_id'])
        return response

    @api.expect(events)
    @api.doc(parser=parser)
    def put(self):
        """ updates data from `events` table  """
        data = request.get_json()
        response = event.update_event(data)
        return response

    @api.expect(events)
    @api.doc(parser=parser)
    def post(self):
        """ adds data to `events` table  """
        data = request.get_json()
        response = event.add_event(data)
        return response
