import unittest
import json
import pprint
from run import app

class TestClass(unittest.TestCase):

    def setUp(self):
        # self.app = create_app("testing")
        self.client = app.test_client

        self.rideoffer_body = {
            "rideId": 1,
            "driver": "Amos Quito",
            "Pickup Point": "kanjokya",
            "Destination": "Bukoto street",
            "Time": "7:00pm",
            "done":False
            }

    def test_create_rideoffer(self):
        """Test API can create a Ride offer """
        res = self.client().post('/api/v1/rides', data=self.rideoffer_body)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Pickup Point', str(res.data))





if __name__ == "__main__":
    unittest.main()
