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

        self.assertEqual(res.status_code, 404)
        self.assertTrue(res.status_code, 201)

    def test_get_all_rides(self):
        """Test API can view all."""
        res = self.client().get('api/v1/rides',
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_all_requests(self):
        """Test API can view all."""
        res = self.client().get('api/v1/requests',
                                content_type='application/json')
        self.assertEqual(res.status_code, 404)
        self.assertTrue(res.status_code, 200)

    def test_fetch_single_id(self):
        """Test API can view single id."""
        res = self.client().get('/api/v1/rides/1',
                                content_type='application/json')
        reply = res.data
        # self.assertTrue(len(reply.rideffer_body), 1)
        self.assertEqual(res.status_code, 404)

    def test_create_rides_fail(self):
        self.rideoffer_body['driver'] = '   '
        res = self.client().post(
            '/v1/rides',
            content_type='application/json')
        reply = res.data
        self.assertTrue(
            self.rideoffer_body['driver'],  'One of the required fields is empty')
        self.assertEqual(res.status_code, 404)
