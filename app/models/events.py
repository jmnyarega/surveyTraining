from sqlalchemy.sql import func

from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from app import db


class Events(db.Model):
    '''
    Defines properties for an event to generate
    an event table in the database
    '''
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    description = Column(String(80), nullable=False)
    start_date = Column(DateTime(), server_default=func.now())
    end_date = Column(DateTime(), server_default=func.now())
    token = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(
        self,
        name='',
        description='',
        start_date=func.now(),
        end_date=func.now(),
        token=''
    ):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.token = token

    def __str__(self):
        return "Event(id='%s')" % self.id

    def add_event(self, data):
        event = Events(
            name=data.get('name'),
            description=data.get('description')
        )
        db.session.add(event)
        db.session.commit()
        return event.__str__()

    def format_date(self, date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def get_events(self):
        events = Events.query.all()
        event_list = []
        for event in events:
            event_dict = {}
            event_dict['id'] = event.id
            event_dict['name'] = event.name
            event_dict['description'] = event.description
            event_dict['start_date'] = self.format_date(event.start_date)
            event_dict['end_date'] = self.format_date(event.end_date)
            event_list.append(event_dict)
        return event_list

    def delete_event(self, event_id):
        event = Events.query.filter_by(id=event_id).first()
        db.session.delete(event)
        db.session.commit()

    def update_event(self, data):
        event = Events.query.filter_by(id=data.get('id')).first()
        event.name = data.get('name')
        event.description = data.get('description')
        if data.get('start_date'):
            event.start_date = data.get('start_date')
        if data.get('start_date'):
            event.end_date = data.get('end_date')
        db.session.add(event)
        db.session.commit()
