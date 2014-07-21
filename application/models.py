from google.appengine.ext import ndb
from flask.ext.login import UserMixin
from application.app import login_manager


class User(UserMixin, ndb.Model):
    '''User Model'''

    created = ndb.DateTimeProperty(auto_now_add=True)
    email = ndb.StringProperty()
    google_user = ndb.UserProperty()
    logined = ndb.DateTimeProperty()
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    weight = ndb.IntegerProperty()
    height = ndb.IntegerProperty()

    def get_id(self):
        '''Return User id for using in flask-login'''
        return self.key.id()

    @classmethod
    def by_google(cls, google_user):
        '''Create User entity by Google User Api object'''
        user = User(google_user=google_user, name=google_user.nickname())
        user.name = google_user.nickname()
        user.email
        user.put()
        return user


@login_manager.user_loader
def get_user(user_id):
    return User.get_by_id(user_id)
