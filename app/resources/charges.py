from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('bills')
parser.add_argument('rent')
parser.add_argument('notes')
parser.add_argument('paid')
parser.add_argument('user_id')
parser.add_argument('rent_calculation_id')

class ChargeListAPI(Resource):
    @marshal_with(models.Charge.__json__())
    def get(self):
        return models.Charge.query.all()

    def post(self):
        args = parser.parse_args()

        if args.user_id is None:
            return "user_id not set", 400

        if args.paid is None:
            args.paid = 0
        else:
            args.paid = args.paid == "True"

        charge = models.Charge(bills=args.bills, rent=args.rent, notes=args.notes, paid=args.paid, user_id=args.user_id, rent_calculation_id=args.rent_calculation_id)

        db.session.add(charge)
        db.session.commit()

        return charge.id, 201

class ChargeAPI(Resource):
    @marshal_with(models.Charge.__json__())
    def get(self, id):
        return models.Charge.query.get(id)

    def put(self, id):
        charge =  models.Charge.query.get(id)
        args = parser.parse_args()

        if args.bills is not None:
            charge.bills = args.bills

        if args.rent is not None:
            charge.rent = args.rent

        if args.notes is not None:
            charge.notes = args.notes

        if args.paid is not None:
            charge.paid = args.paid == "True"

        if args.user_id is not None:
            charge.user_id = args.user_id

        if args.rent_calculation_id is not None:
            charge.rent_calculation_id = args.rent_calculation_id

        db.session.commit()
        return

    def delete(self, id):
        charge =  models.Charge.query.get(id)

        db.session.delete(charge)
        db.session.commit()

        return

api.add_resource(ChargeListAPI, '/charges', endpoint = 'chargeList')
api.add_resource(ChargeAPI, '/charges/<int:id>', endpoint = 'charge')