from ..tracks import tracks
from flask import render_template


@tracks.route('test')
def test():
    # return render_template('home.html')
    assert True is False
    return 'Hello tracks! (test)'


@tracks.route('/')
def home():
    # return render_template('home.html')
    return 'Hello tracks!'
