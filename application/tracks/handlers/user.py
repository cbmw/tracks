import json
from application.models import User
from flask import redirect
from flask.ext.login import login_user, current_user
from flask.views import MethodView
from google.appengine.api import users
from gaejson import GaeJSONEncoder


class CurrentUser(MethodView):
    def get(self):
        user = users.get_current_user()
        if user:
            return json.dumps(user, cls=GaeJSONEncoder)


class UserLogin(MethodView):
    def get(self):
        google_user = users.get_current_user()
        print(google_user)
        if not google_user:
            return redirect(users.create_login_url())
        else:
            # Get User associated with google_user
            user = User.query(User.google_user == google_user).get()
            if user:
                print('User exists', user)
            else:
                user = User.create(google_user)
                print('User created', user)
            login_user(user)
            return 'test'
