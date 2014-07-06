import json
from google.appengine.api.users import User


def user_encoder(obj):
    return {'id': obj.user_id(),
            'email': obj.email(),
            'auth_domain': obj.auth_domain(),
            'nickname': obj.nickname()}


GAE_TYPE_ENCODER = {
    User: user_encoder,
}


class GaeJSONEncoder(json.JSONEncoder):
    """ Extend JSONEncoder for GAE types support """

    def default(self, obj):
        obj_type = type(obj)
        encoder = GAE_TYPE_ENCODER.get(obj_type)
        if encoder:
            return encoder(obj)
        return json.JSONEncoder.default(self, obj)
