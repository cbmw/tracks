from gae_app.tracks.handlers import HomeView
from flask import Blueprint


tracks = Blueprint('tracks', __name__)
tracks.add_url_rule('/', view_func=HomeView.as_view('home'))
