from app import db
from flask.ext.restful import fields


class Charge(db.Model):
    __tablename__ = 'charges'
    id = db.Column(db.Integer, primary_key=True)
    bills = db.Column(db.Float, index=False, unique=False)
    rent = db.Column(db.Float, index=False, unique=False)
    notes = db.Column(db.String(64), index=False, unique=False)
    paid = db.Column(db.Boolean, index=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rent_calculation_id = db.Column(db.Integer, db.ForeignKey('rent_calculations.id'))

    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'bills': fields.Float,
            'rent': fields.Float,
            'notes': fields.String,
            'paid': fields.Boolean
        }

        if group == 'flat':
            return _json

        from app.models import User
        _json['user'] = fields.Nested(User.__json__('flat'))

        return _json

    def __repr__(self):
        return '<Charge %r>' % (self.id)
