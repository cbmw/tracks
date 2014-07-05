from application.app import create_app
from application import settings
from werkzeug import DebuggedApplication


app = create_app(settings)

if app.config['DEBUG']:
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
