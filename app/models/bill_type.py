from app import db
from flask.ext.restful import fields

class BillType(db.Model):
    __tablename__ = 'bill_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=False)
    bills = db.relationship("Bill", backref='bill_types', lazy='dynamic')

    # Defines if bill should be paid by homeowner
    chargeable = db.Column(db.Boolean, index=False, unique=False)

    # Defines if bill has to be paid by tenants
    should_calculate = db.Column(db.Boolean, index=False, unique=False)

    @staticmethod
    def __json__(group=None):
        _json = {
            'id': fields.Integer,
            'name': fields.String,
            'reason': fields.String,
            'should_calculate': fields.Boolean,
            'chargeable': fields.Boolean
        }

        return _json

    def __repr__(self):
        return '<BillType %r>' % (self.id)
