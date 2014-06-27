from flask import Flask
from gae_app import urls


def register_blueprints(app):
    app.register_blueprint(urls.tracks)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Register blueprints
    # from gae_app.tracks import tracks
    # app.register_blueprint(tracks, url_prefix="/")
    register_blueprints(app)
    return app
