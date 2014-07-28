import unittest
import sys
import os
import json
sys.path.append('/opt/google_appengine/')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from google.appengine.datastore import datastore_stub_util
from google.appengine.ext import testbed
from application.app import app_factory
from flask.ext.login import current_user


class UserTest(unittest.TestCase):
    def setUp(self):
        self.app = app_factory()
        self.client = self.app.test_client()
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()
        # Create a consistency policy that will simulate the High Replication
        # consistency model.
        self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(
            probability=0)
        # Initialize the datastore and memcache stubs with this policy.
        self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)
        self.testbed.init_memcache_stub()
        # Setup current user
        self.testbed.setup_env(
            USER_EMAIL='test@example.com',
            USER_ID='123',
            USER_IS_ADMIN='1',
            overwrite=True)

    def tearDown(self):
        self.testbed.deactivate()

    def testLogin(self):
        self.client.get('/login')
        rv = self.client.get('/api/user/current')
        user = json.loads(rv.data)
        self.assertEqual('test@example.com', user['email'])
        self.assertEqual(1, user['id'])
        self.assertEqual('123', user['google_user']['id'])

    def testLogout(self):
        self.testLogin()
        res = self.client.get('/logout')
        self.assertEqual(302, res.status_code)
        res = self.client.get('/api/user/current')
        self.assertEqual(302, res.status_code)


if __name__ == '__main__':
    unittest.main()
