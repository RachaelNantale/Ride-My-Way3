import unittest
import json
import pprint
from app import create_app
from tests.BaseTest import BaseTest


class TestClass(BaseTest):

    def test_create_rideoffer(self):
        """Test API can create a Ride offer """
        res = self.client().post('/api/v1/rides/',
                                 content_type='application/json',
                                 data=json.dumps(self.rideoffer_body))

        self.assertEqual(res.status_code, 201)

    # def test_get_all_rides(self):
    #     """Test API can view all."""
    #     print(res)
    #     self.assertEqual(res.status_code, 201)
    #     res = self.client().get('/api/v1/rides')
    #     print(res)
    #     self.assertEqual(res.status_code, 200)

    # def test_fetch_single_id(self):
    #     """Test API can view single id."""
    #     reply = resp.data
    #     self.assertEqual(len(reply.rideffer_body), 1)
    #     self.assertEqual(resp.status_code, 200)
