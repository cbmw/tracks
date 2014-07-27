import datetime
import json
import types
from google.appengine.api import users
from google.appengine.ext import ndb


class GaeJSONEncoder(json.JSONEncoder):
    """ Extend JSONEncoder for GAE types support """

    def _datetime_encoder(obj):
        '''ISO 8601 format'''
        zone = '' if getattr(obj, 'tzinfo', True) else 'Z'
        return obj.isoformat() + zone

    def _user_encoder(obj):
        '''google.appengine.api.users.User object json encoder'''
        return {'id': obj.user_id(),
                'email': obj.email(),
                'auth_domain': obj.auth_domain(),
                'nickname': obj.nickname()}

    def _model_encoder(obj):
        '''google.appengine.ext.ndb.Model and subclasses encoder'''
        obj_dict = obj.to_dict()
        obj_dict['kind'] = obj.key.kind()
        obj_dict['id'] = obj.key.id()
        return obj_dict

    encoders = {
        users.User: _user_encoder,
        ndb.model.MetaModel: _model_encoder,
        datetime.datetime: _datetime_encoder,
    }

    def default(self, obj):
        return self.get_encoder(obj)

    def get_encoder(self, obj):
        obj_type = type(obj)
        if obj_type not in self.encoders and hasattr(obj, '__metaclass__'):
            obj_type = obj.__metaclass__
        encoder = self.encoders.get(obj_type)
        if encoder:
            return encoder(obj)
        return json.JSONEncoder.default(self, obj)
