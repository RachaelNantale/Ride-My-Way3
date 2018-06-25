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

    def post(self):
        """
        Allows users to login to their accounts
        """
        args = self.reqparse.parse_args()
        user_login = User(args['username'], args['password'])
        print(user_login.username)
        # user = user_login.to_json()
        for user in USERS:
            if user.username:
                access_token = user.generate_token()
                return make_response(jsonify({"token": access_token,
                                              "message": "User logged in"
                                              }), 200)
            return make_response(jsonify({"message": "wrong credential"}), 401)


api.add_resource(Signup, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
