from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('amount')
parser.add_argument('reason')
parser.add_argument('paid')
parser.add_argument('user_id')

class ChargeListAPI(Resource):
    @marshal_with(models.Charge.__json__())
    def get(self):
        return models.Charge.query.all()

    def post(self):
        args = parser.parse_args()

        if args.amount is None:
            return "amount not set", 400

        if args.user_id is None:
            return "user_id not set", 400

        if args.paid is None:
            args.paid = 0

        charge = models.Charge(amount=args.amount, reason=args.reason, paid=args.paid, user_id=args.user_id)

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

        if args.amount is not None:
            charge.amount = args.amount

        if args.reason is not None:
            charge.reason = args.reason

        if args.paid is not None:
            charge.paid = args.paid

        if args.user_id is not None:
            charge.user_id = args.user_id

        db.session.commit()
        return

    def delete(self, id):
        charge =  models.Charge.query.get(id)

        db.session.delete(charge)
        db.session.commit()

        return

api.add_resource(ChargeListAPI, '/charges', endpoint = 'chargeList')
api.add_resource(ChargeAPI, '/charges/<int:id>', endpoint = 'charge')