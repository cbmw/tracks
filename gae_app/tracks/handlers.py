from ..tracks import tracks
from flask import render_template
from flask.views import MethodView


class HomeView(MethodView):
    def get(self):
        return 'Hello tracks! (HomeView)'


@tracks.route('test')
def test():
    # return render_template('home.html')
    assert True is False
    return 'Hello tracks! (test)'


@tracks.route('/')
def home():
    # return render_template('home.html')
    return 'Hello tracks!'
