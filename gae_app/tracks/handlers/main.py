from flask.views import MethodView
from google.appengine.api import users


class MainView(MethodView):
    def get(self):
        return 'Hello tracks! (HomeView) <a href="{}">login</a>'.format(
            users.create_login_url())
