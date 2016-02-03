from app import db
from flask.ext.restful import fields

class Bill(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, index=False, unique=False)
    bill_type_id = db.Column(db.Integer, db.ForeignKey('bill_types.id'))
    notes = db.Column(db.String(64), index=False, unique=False)
    paid = db.Column(db.Boolean, index=False, unique=False)
    rent_calculation_id = db.Column(db.Integer, db.ForeignKey('rent_calculations.id'))

    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'amount': fields.Float,
            'notes': fields.String,
            'paid': fields.Boolean,
            'bill_type_id': fields.Integer,
        }

        from app.models import BillType
        _json['bill_type'] = fields.Nested(BillType.__json__())

        return _json

    def __repr__(self):
        return '<Bill %r>' % (self.id)