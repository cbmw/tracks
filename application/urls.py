from application.tracks.handlers.user import CurrentUser, UserLogin, UserLogout
from application.tracks.handlers.main import MainView
from flask import Blueprint


tracks = Blueprint('tracks', __name__)
tracks.add_url_rule('/', view_func=MainView.as_view('main'))
tracks.add_url_rule('/login', view_func=UserLogin.as_view('login'))
tracks.add_url_rule('/logout', view_func=UserLogout.as_view('logout'))
tracks.add_url_rule('/api/user/current',
                    view_func=CurrentUser.as_view('currentuser'))
