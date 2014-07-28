from application.tracks.handlers.user import UserLogin, UserLogout
from application.tracks.handlers.main import MainView
from application.api.handlers.user import UserView
from flask import Blueprint


tracks = Blueprint('tracks', __name__)
api = Blueprint('api', __name__)

# App
tracks.add_url_rule('/', view_func=MainView.as_view('main'))
tracks.add_url_rule('/login', view_func=UserLogin.as_view('login'))
tracks.add_url_rule('/logout', view_func=UserLogout.as_view('logout'))

# Api
api.add_url_rule('/api/user',
                 view_func=UserView.as_view('user'))
