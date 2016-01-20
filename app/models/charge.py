from app import db
from flask.ext.restful import fields

class Charge(db.Model):
    __tablename__ = 'charges'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, index=False, unique=False)
    reason = db.Column(db.String(64), index=False, unique=False)
    paid = db.Column(db.Boolean, index=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'amount': fields.Float,
            'reason': fields.String,
            'paid': fields.Boolean,
            'uri': fields.Url('charge')
        }

        if group == 'flat':
            return _json

        from app.models import Room, User
        _json['user'] = fields.Nested(User.__json__('flat'))

        return _json

    def __repr__(self):
        return '<Charge %r>' % (self.id)