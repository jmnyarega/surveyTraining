from flask_restplus import Resource, fields
from flask import request

from .main import api, parser
from app import db
from .models.helpers import Helpers
from .models.events import Events
from .models.session import Session

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
                return self.formart_event_response(event_obj)
            if event_obj:
                return self.formart_event_response(event_obj)
            else:
                return helper.handle_404_success([])
        except Exception as e:
            return helper.handle_500_error(str(e))

    def formart_event_response(self, event_obj):
        event_list = []
        for event in event_obj:
            event_dict = {}
            sessions = Session.query.filter_by(event_id=event.id).all()
            session_list = []
            for session in sessions:
                session_dict = {}
                session_dict["id"] = session.id
                session_dict["event_id"] = session.event_id
                session_dict["created_at"] = session.created_at.isoformat()
                session_dict["start_date"] = session.start_date.isoformat()
                session_dict["user_id"] = session.user_id
                session_list.append(session_dict)
            event_dict["created_at"] = event.created_at.isoformat()
            event_dict["description"] = event.description
            event_dict["end_date"] = event.end_date.isoformat()
            event_dict["id"] = event.id
            event_dict["name"] = event.name
            event_dict["start_date"] = event.start_date.isoformat()
            event_dict["token"] = event.token
            event_dict["user_id"] = event.user_id
            event_dict["sessions"] = session_list
            event_list.append(event_dict)
        return { "data": event_list }

    def delete(self, event_id):
        """ deletes data from `events` table  """
        try:
            event_obj = Events.query.filter_by(id=event_id).first()
            db.session.delete(event_obj)
            db.session.commit()
            return helper.handle_204_delete_success(
                    'Event Successfully deleted'
                    )
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
            updated_obj = Events.query.filter_by(id=data.get('id')).first()
            returnObj = helper.serialize([updated_obj], events_marshal)
            return helper.handle_201_success([returnObj])
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
                description=data.get('description'),
                user_id=data.get('user_id'),
            )
            db.session.add(event_obj)
            db.session.commit()
            added_event = Events.query.filter_by(user_id=data.get('user_id')).order_by(Events.id.desc()).first()
            returnObj = helper.serialize([added_event], events_marshal)
            return helper.handle_201_success(returnObj)
        except Exception as e:
            return helper.handle_400_bad_request(str(e))
