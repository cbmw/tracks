from flask.views import MethodView
from flask import render_template
from google.appengine.api import users


class MainView(MethodView):
    def get(self):
        # return 'Hello tracks! (HomeView) <a href="{}">login</a>'.format(
        #    users.create_login_url())
        return render_template('layout.html', login_url=users.create_login_url())
