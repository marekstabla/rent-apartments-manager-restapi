from flask.ext.restful import fields, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('apartment_id')

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id'))
    tenants = db.relationship('User', backref='room', lazy='dynamic')

    @staticmethod
    def __json__(group=None):
        from app.models import Apartment

        _json = {
            'id': fields.Integer,
            'name': fields.String,
            'uri': fields.Url('room')
        }

        if group == 'flat':
            return _json

        from app.models import User
        _json['tenants'] = fields.List(fields.Nested(User.__json__('flat')))
        _json['apartment'] = fields.Nested(Apartment.__json__('flat'))

        return _json


    def __repr__(self):
        return '<Room %r>' % (self.name)
