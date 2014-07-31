import json
from flask import jsonify
from flask.views import MethodView
from flask.ext.login import current_user
from gaejson import GaeJSONEncoder


class UserView(MethodView):
    def get(self):
        if current_user:
            return json.dumps(current_user, cls=GaeJSONEncoder)
