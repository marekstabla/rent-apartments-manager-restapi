from app import db
from flask.ext.restful import fields

class Apartment(db.Model):
    __tablename__ = 'apartments'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True, unique=False)
    rooms = db.relationship('Room', backref='apartment', lazy='dynamic')
    rent_calculations = db.relationship('RentCalculation', backref='apartment', lazy='dynamic', order_by="desc(RentCalculation.)")


    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'location': fields.String,
            'uri': fields.Url('apartment')
        }

        if group == 'flat':
            return _json

        from app.models import Room, RentCalculation
        _json['rooms'] = fields.List(fields.Nested(Room.__json__()))
        _json['rent_calculations'] = fields.List(fields.Nested(RentCalculation.__json__('flat')))

        return _json

    def __repr__(self):
        return '<Apartment %r>' % (self.id)