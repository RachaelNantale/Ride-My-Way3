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

    def test_user_logged_in(self):
        self.client().post('/api/v1/auth/signup',
                           content_type='application/json',
                           data=json.dumps(self.user_body))
        res = self.client().post('/api/v1/auth/login',
                                 content_type='application/json',
                                 data=json.dumps(self.loginlist))
        reply = res.data.decode()
        self.assertEqual(res.status_code, 200)

    def test_create_rideoffer(self):
        """Test API can create a Ride offer """
        res = self.client().post('/api/v1/rides',
                                 content_type='application/json',
                                 headers=dict(
                                     Authorization='Bearer' + 'token'),
                                 data=json.dumps(self.rideoffer_body))
        reply = res.data.decode()

    
