class Helpers():

    def __init__(self):
        pass

    def format_date(self, date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def unpack_query_session_object(self, object):
        try:
            session_list = []
            for session in object:
                session_dict = {}
                session_dict['id'] = session.id
                session_dict['event_id'] = session.event_id
                session_dict['user_id'] = session.user_id
                session_dict['start_date'] = self.format_date(
                    session.start_date)
                session_dict['created_at'] = self.format_date(
                    session.created_at)
                session_list.append(session_dict)
            return session_list
        except Exception as e:
            session_list = []
            session_dict = {}
            session_dict['id'] = object.id
            session_dict['event_id'] = object.event_id
            session_dict['user_id'] = object.user_id
            session_dict['start_date'] = self.format_date(object.start_date)
            session_dict['created_at'] = self.format_date(object.created_at)
            session_list.append(session_dict)
            return session_list

    def unpack_query_roles_object(self, object):
        try:
            session_list = []
            for session in object:
                session_dict = {}
                session_dict['id'] = session.id
                session_dict['name'] = session.name
                session_dict['created_at'] = self.format_date(
                    session.created_at)
                session_list.append(session_dict)
            return session_list
        except Exception as e:
            session_list = []
            session_dict = {}
            session_dict['id'] = object.id
            session_dict['name'] = object.name
            session_dict['created_at'] = self.format_date(object.created_at)
            session_list.append(session_dict)
            return session_list
