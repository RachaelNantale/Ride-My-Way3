import uuid
import json
import jwt
from datetime import datetime, timedelta
from flask import jsonify, current_app, make_response
import re
from dbHandler import MyDatabase
db = MyDatabase()


class User:
    """
    Class to represent the User model
    """

    def __init__(self, username, email="", password="", phone=""):
        self.id = uuid.uuid4().hex
        self.username = username.strip(" ")
        self.email = email.strip(" ")
        self.password = password.strip(" ")
        self.phone = phone
        self.errors = []

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'phone': self.phone

        }

    def save_to_db(self):
        if validate_user_input(self, self.username, self.email, self.password,
                               self.phone, self.errors):
            sql = "INSERT INTO UserTable values('{}','{}','{}','{}','{}')RETURNING id".format(
                self.id, self.username, self.email, self.password, self.phone)
            return db.create_login(sql)

        return False

    def select_from_db(self, username):
        if validate_user_input(self, self.username,
                               self.password, self.errors):
            sql = "SELECT * FROM UserTable WHERE username = '{}'".format(
                username)
            print(sql)
            return db.user_login(sql)
        return False


def validate_user_input(self, username="", email="", password="",
                        phone="", errors=[]):

    result = True

    if re.compile('[!@#$%^&*:;?><.0-9]').match(username):
        errors.append('Please  donot use symbols')
        result = False

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        errors.append('Enter valid email')
        result = False
    if len(password) < 5:
        errors.append('Password is too short')
        result = False

    if len(phone) < 10:
        errors.append('Phone number is too short')
        result = False

    return True
