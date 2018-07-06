from flask import Flask, jsonify, abort, make_response, Blueprint, current_app
from flask_restful import Api, Resource, reqparse, fields
from app.api.models.user import User
from dbHandler import MyDatabase
from flask_jwt_extended import create_access_token
import datetime
import re
import uuid

app_bps = Blueprint('app_user', __name__)
api = Api(app_bps)

db = MyDatabase()


class Signup(Resource):
    """signup class"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True)
        self.reqparse.add_argument('email', type=str, required=True)
        self.reqparse.add_argument('password', type=str, required=True)
        self.reqparse.add_argument('phone', type=str, required=True)
        super(Signup, self).__init__()

    def post(self):
        """
        Allows users to create accounts
        """
        args = self.reqparse.parse_args()
        new_user = User(args['username'], args['email'],
                        args['password'], args['phone'])
        try:

            created_user = new_user.save_to_db()
            message = 'User Created Successfuly'
            status_code = 201
            status_msg = 'Success with id:'
            return make_response(jsonify({'user': created_user, 'Message': message, 'status': status_msg}), status_code)

        except Exception:

            message = 'An error occured please check again.'
            if len(new_user.errors) > 0:
                message = new_user.errors
            status_code = 400
            status_msg = 'Fail'

            return make_response(jsonify({'Message': message, 'status': status_msg}), status_code)


class Login(Resource):
    """Login class"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True)
        self.reqparse.add_argument('password', type=str, required=True)
        super(Login, self).__init__()

    def post(self):
        _id = str(uuid.uuid1())

        """
        Allows users to login to their accounts
        """

        args = self.reqparse.parse_args()
        users = User(args['username'])
        print(args['username'])
        result = users.select_from_db(args['username'])
        print(result)

        if result is not None:
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=args['username'],
                                               expires_delta=expires)
            return make_response(jsonify({'message': 'user successful logged in',
                                          'token': access_token}))

        return make_response(jsonify({'message': 'User not found.\
                                      Please sign up'}), 400)


api.add_resource(Signup, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
