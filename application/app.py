from flask import Flask
from flask.ext.login import LoginManager


login_manager = LoginManager()


def register_blueprints(app):
    from application import urls
    app.register_blueprint(urls.tracks)


def app_factory(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Login manager
    login_manager.setup_app(app)
    login_manager.login_view = 'user.login'

    # Register blueprints
    # from gae_app.tracks import tracks
    # app.register_blueprint(tracks, url_prefix="/")
    register_blueprints(app)

    return app
