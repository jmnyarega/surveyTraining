from flask import jsonify, make_response
from flask_restplus import marshal


class Helpers():

    def __init__(self):
        pass

    def format_date(self, date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def handle_200_success(self, message):
        return make_response(jsonify(message), 200)

    def handle_201_success(self, message):
        return make_response(jsonify({'message': message}), 201)

    def handle_204_delete_success(self, message):
        return make_response(jsonify({'message': message}), 202)

    def handle_400_bad_request(self, message):
        return make_response(jsonify({'message': message}), 400)

    def handle_401_error(self, message):
        return make_response(jsonify({'message': message}), 401)

    def handle_404_success(self, message):
        return make_response(jsonify({'message': message}), 404)

    def handle_500_error(self, message):
        return make_response(jsonify({'message': message}), 500)

    def serialize(self, sqlalchemy_query, subject, marshal_object):
        return {subject:[marshal(session, marshal_object) for session in sqlalchemy_query]}
