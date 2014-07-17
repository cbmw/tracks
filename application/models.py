from google.appengine.ext import ndb
from flask.ext.login import UserMixin
from application.app import login_manager


class User(UserMixin, ndb.Model):
    """User Model"""

    created_at = ndb.DateTimeProperty(auto_now_add=True)
    google_user = ndb.UserProperty()
    name = ndb.StringProperty()

    def get_id(self):
        return unicode(self.key.id())

    @classmethod
    def create(cls, google_user):
        user = User(google_user=google_user, name=google_user.nickname())
        user.put()
        return user


@login_manager.user_loader
def get_user(id):
    return User.get_by_id(id)
