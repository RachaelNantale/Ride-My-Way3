from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields
from app.api.models.user import User
from app.utility import ValidateRideData
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

        USERS.append(new_user)

        return make_response(jsonify({
            'message': 'User successfull created with id: ' + new_user.get_id()
        }), 201)


class Login(Resource):
    """Login class"""

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True)
        self.parser.add_argument('password', type=str, required=True)
        super(Login, self).__init__()

    def post(self):
        """
        Allows users to login to their accounts
        """
        args = self.parser.parse_args()
        email = args['username']
        password = args['password']

        for user in USERS:
            if username == user['username'] and password == user['password']:
                access_token = generate_token(user['email'])
                return make_response(jsonify({"token": access_token,
                                              "message": "User logged in"
                                              }), 200)
        return make_response(jsonify({"message": "wrong credentials"}), 401)


api.add_resource(Signup, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
