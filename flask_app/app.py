from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Register blueprints
    from flask_app.tracks import tracks
    app.register_blueprint(tracks, url_prefix="/")
    return app
