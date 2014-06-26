from flask_app.app import create_app
from flask_app import settings
from werkzeug import DebuggedApplication


app = create_app(settings)

if app.config['DEBUG']:
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
