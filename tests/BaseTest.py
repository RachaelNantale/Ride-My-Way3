import unittest
import json
from app import create_app
from dbHandler import MyDatabase


class BaseTest (unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client
        db = MyDatabase()
        db.create_tables()

        self.rideoffer_body = {
            "driver": "Amos Quito",
            "pickup_point": "kanjokya",
            "Destination": "Bukoto street",
            "Time": "7:00pm"
        }
        self.request_body = {
            "passenger": "Amos Quito",
            "pickup_point": "kanjokya",
            "Destination": "Bukoto street",
            "Time": "7:00pm"

        }
        self.user_body = {
            "username": "rachael",
            "email": "rachael@sample.com",
            "password": "123abc",
            "phone": "0708888999"
        }
        self.loginlist = {
            'username': 'rachael',
            'password': '123abc'
        }

    def test_login(self):
        self.client().post('/api/v1/auth/signup',
                           content_type='application/json',
                           data=json.dumps(self.user_body))
        self.client().post('/api/v1/auth/login',
                           content_type='application/json',
                           data=json.dumps(self.loginlist))

    def tearDown(self):
        db = MyDatabase()
        db.drop_tables()
        db.create_tables()


if __name__ == "__main__":
    unittest.main()
