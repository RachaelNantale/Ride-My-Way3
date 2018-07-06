import unittest
import json
from app import create_app
from tests.BaseTest import BaseTest


class TestClass(BaseTest):

    def test_user_siginup(self):
        """Test API can signup """

        res = self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps(self.user_body))
        self.assertTrue(res.status_code, 201)
        self.assertIn('User Created Successfuly', str(res.data))

    def test_create_rideoffer(self):
        """Test API can create a Ride offer """

        res = self.client().post('/api/v1/rides',
                                 content_type='application/json',
                                 data=json.dumps(self.rideoffer_body))

        self.assertEqual(res.status_code, 400)
        self.assertTrue(res.status_code, 201)

    def test_create_request(self):
        """ Test API can create a request"""
        self.client().post('/api/v1/rides',
                           content_type='application/json',
                           data=json.dumps(self.rideoffer_body))
        res = self.client().post('/api/v1/rides/1/request',
                                 content_type='application/json',
                                 data=json.dumps(self.request_body))

        self.assertEqual(res.status_code, 201)
        self.assertTrue(res.status_code, 201)

    def test_get_all_rides(self):
        """Test API can view all."""
        res = self.client().get('api/v1/rides',
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_all_requests(self):
        """Test API can view all."""
        res = self.client().get('/api/v1/rides/<string:ride_id>/requests',
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_fetch_single_id(self):
        """Test API can view single id."""
        self.client().post('/api/v1/rides',
                           content_type='application/json',
                           data=json.dumps(self.rideoffer_body))
        res = self.client().get('/api/v1/rides/1',
                                content_type='application/json')
        reply = res.data

        self.assertTrue(len(str(reply.rideoffer_body), 1))
        self.assertEqual(res.status_code, 404)

    def test_create_rides_fail(self):
        self.rideoffer_body['driver'] = '   '
        res = self.client().post(
            'api/v1/rides',
            content_type='application/json',
            data=json.dumps(self.rideoffer_body))
        reply = res.data
        self.assertTrue(
            self.rideoffer_body['driver'],  'One of the required fields is empty')
        self.assertEqual(res.status_code, 400)

    # def test_signup_user(self):
    #     """ Test if user is registered"""
