import json
from application.models import User
from flask import redirect, url_for
from flask.ext.login import login_user, current_user, logout_user
from flask.views import MethodView
from google.appengine.api import users
from gaejson import GaeJSONEncoder


class CurrentUser(MethodView):
    def get(self):
        print(current_user)
        user = users.get_current_user()
        if user:
            return json.dumps(user, cls=GaeJSONEncoder)


class UserLogout(MethodView):
    def get(self):
        google_user = users.get_current_user()
        if google_user:
            return redirect(users.create_logout_url(url_for('tracks.logout')))
        if current_user.is_authenticated():
            logout_user()
        return redirect(url_for('tracks.main'))


class UserLogin(MethodView):
    def get(self):
        if current_user.is_authenticated():
            return redirect(url_for('tracks.main'))
        google_user = users.get_current_user()
        if not google_user:
            return redirect(users.create_login_url(url_for('tracks.login')))
        else:
            # Get User associated with google_user
            user = User.query(User.google_user == google_user).get()
            if not user:
                user = User.by_google(google_user)
            login_user(user)
            return redirect(url_for('tracks.main'))
