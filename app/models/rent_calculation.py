from app import db
from flask.ext.restful import fields

class RentCalculation(db.Model):
    __tablename__ = 'rent_calculations'
    id = db.Column(db.Integer, primary_key=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id'))
    bills = db.relationship('Bill', backref='rent_calculation', lazy='dynamic')
    charges = db.relationship('Charge', backref='rent_calculation', lazy='dynamic')
    notes = db.Column(db.String(64), index=False, unique=False)


    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'notes': fields.String
        }

        if group == 'flat':
            return _json

        from app.models import Apartment, Bill, Charge
        _json['apartment'] = fields.Nested(Apartment.__json__('flat'))
        _json['bills'] = fields.List(fields.Nested(Bill.__json__('flat')))
        _json['charges'] = fields.List(fields.Nested(Charge.__json__('flat')))

        return _json

    def __repr__(self):
        return '<RentCalculation %r>' % (self.id)