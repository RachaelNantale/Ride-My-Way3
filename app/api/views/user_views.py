from flask import Flask, jsonify, abort, make_response, Blueprint, current_app
from flask_restful import Api, Resource, reqparse, fields
from app.api.models.user import User
from app.utility import ValidateRideData
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

        if args['username'].strip() == "" or len(args['username'].strip()) < 2:
            return make_response(jsonify({"message":
                                          "invalid, Enter name please"}), 400)

        if re.compile('[!@#$%^&*:;?><.0-9]').match(args['username']):
            return make_response(jsonify({"message":
                                          "Invalid characters not allowed"}
                                         ), 400)

        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", args['email']):
            return make_response(jsonify({"message":
                                          "Enter valid email"}), 400)

        if args['password'].strip() == "":
            return make_response(jsonify({"message": "Enter password"}), 400)

        if len(args['password']) < 5:
            return make_response(jsonify({"message":
                                          "Password is too short, < 5"}), 400)

        if len(args['phone']) < 10:
            return make_response(jsonify({"message":
                                          "Phone number is too short"}), 400)

        print(new_user)

        USERS.append(new_user)
        for user in USERS:
            print(user.username)
        # print(USERS)

        return make_response(jsonify({
            'message': 'User successfull created with id: ' + new_user.get_id()
        }), 201)


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
