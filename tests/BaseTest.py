import unittest
import json
import pprint
from app import create_app


class BaseTest (unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client

        self.rideoffer_body = {
            "driver": "Amos Quito",
            "pickup_point": "kanjokya",
            "Destination": "Bukoto street",
            "Time": "7:00pm",
        }

        res = self.client().post('/api/v1/rides/',
                                 content_type='application/json',
                                 data=json.dumps(self.rideoffer_body))

        resp = self.client().get('/api/v1/rides/<int:id>',
                                 content_type='application/json',
                                 data=json.dumps(self.rideoffer_body))

        res = self.client().post('/api/v1/rides',
                                 content_type='application/json',
                                 data=json.dumps(self.rideoffer_body))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
