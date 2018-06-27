import uuid
import json
import jwt
from app.utility import RideOffers
from datetime import datetime, timedelta
from flask import jsonify, current_app


class User:
    """
    Class to represent the User model
    """

    def __init__(self, username, email=None, password=None, phone=None):
        self.id = uuid.uuid4().hex
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_phone(self):
        return self.phone

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'phone': self.phone

        }

    def use_token(parser):
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        if not args['token']:
            return {"status": False, "message": "Token is missing"}
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return {"status": False, "message": decoded["message"]}
        return {"status": True, "decoded": decoded}

    def generate_token(id):
        """Generates the access token to be used as the Authorization header"""

        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=40),
                'iat': datetime.utcnow(),
                'sub': id
            }
            jwt_string = jwt.encode(
                payload,
                'secret',
                algorithm='HS256'
            ).decode('UTF-8')
            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    def decode_token(token):
        """Decode the access token to get the payload and return
        id """
        try:
            payload = jwt.decode(token, 'secret')
            return jsonify({
                "id": payload['sub'],
                "status": "Success"
            })
        except jwt.ExpiredSignatureError:
            return jsonify({
                "status": "Failure",
                "message": "Expired token. Please log in to get a new token"
            })
        except jwt.InvalidTokenError:
            return jsonify({
                "status": "Failure",
                "message": "Invalid token. Please register or login"
            })
