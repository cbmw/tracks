import unittest
import sys
import os
import json
sys.path.append('/opt/google_appengine/')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from google.appengine.ext import testbed
from google.appengine.api import users
from gaejson import GaeJSONEncoder


class GaeJSONEncoderTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testUserEncoding(self):
        self.testbed.setup_env(
            USER_EMAIL='test@example.com',
            USER_ID='123',
            USER_IS_ADMIN='1',
            USER_NICKNAME='Test user',
            overwrite=True)
        user = users.get_current_user()
        juser = json.loads(GaeJSONEncoder().encode(user))
        self.assertEqual('123', juser['id'])
        self.assertEqual('test@example.com', juser['email'])
        self.assertEqual('Test user', juser['nickname'])


if __name__ == '__main__':
    unittest.main()
