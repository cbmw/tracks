from application.app import app_factory
from application import settings
from flask.ext.login import LoginManager
from werkzeug import DebuggedApplication

app = app_factory(settings)

if app.config['DEBUG']:
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
