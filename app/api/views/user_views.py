from flask import Flask, jsonify, abort, make_response, Blueprint, current_app
from flask_restful import Api, Resource, reqparse, fields
from app.api.models.user import User
# from app.utility import ValidateRideData
import jwt
from datetime import datetime, timedelta
import re

app_bps = Blueprint('app_user', __name__)
api = Api(app_bps)

USERS = []


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
        print(new_user)

        if new_user.save_to_db():
            print(new_user)
            message = 'User Created Successfuly'
            status_code = 201
            status_msg = 'Success'

        else:
            message = 'User Not Created.'
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

        args = self.reqparse.parse_args()

    def post(self):
        """
        Allows users to login to their accounts
        """
        args = self.reqparse.parse_args()

        for user in USERS:
            if user.username == args['username'] and user.password == args['password']:
                # access_token = user.generate_token()
                access_token = jwt.encode(
                    {'usernme': user.username, 'exp': datetime.utcnow() +
                     timedelta(minutes=40)}, "secret")
                return make_response(jsonify({"token":
                                              access_token.decode('UTF-8'),
                                              "message": "User logged in"
                                              }), 200)
            return make_response(jsonify({"message":
                                          "Check your password or username"}
                                         ), 401)
        return make_response(jsonify({"message":
                                      "User not found. Please Sign Up."}), 404)


api.add_resource(Signup, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
