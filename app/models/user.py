from app import db
from flask.ext.restful import fields

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True, unique=False)
    lastName = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    telephoneNumber = db.Column(db.String(20), index=True, unique=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))

    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'firstName': fields.String,
            'lastName': fields.String,
            'email': fields.String,
            'telephoneNumber': fields.String,
            'uri': fields.Url('user')
        }

        if group == 'flat':
            return _json

        from app.models import Room
        _json['room'] = fields.Nested(Room.__json__('flat'))

        return _json
