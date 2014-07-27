import unittest
import sys
import os
import json
sys.path.append('/opt/google_appengine/')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from google.appengine.datastore import datastore_stub_util
from google.appengine.ext import testbed
from google.appengine.api import users
from gaejson import GaeJSONEncoder
from application.models import User


class GaeJSONEncoderTest(unittest.TestCase):
    def setUp(self):
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

    def testUserEncoding(self):
        user = users.get_current_user()
        juser = json.loads(GaeJSONEncoder().encode(user))
        self.assertEqual('123', juser['id'])
        self.assertEqual('test@example.com', juser['email'])
        self.assertEqual('test@example.com', juser['nickname'])

    def testUserModelEncoding(self):
        current_user = users.get_current_user()
        user = User.by_google(current_user)
        # check models.User json encoding
        juser = json.loads(GaeJSONEncoder().encode(user))
        self.assertEqual('test@example.com', juser['email'])


if __name__ == '__main__':
    unittest.main()
