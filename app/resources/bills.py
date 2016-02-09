from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('amount')
parser.add_argument('bill_type_id')
parser.add_argument('notes')
parser.add_argument('paid')
parser.add_argument('rent_calculation_id')

class BillListAPI(Resource):
    @marshal_with(models.Bill.__json__())
    def get(self):
        return models.Bill.query.all()

    def post(self):
        args = parser.parse_args()

        if args.amount is None:
            return "amount not set", 400

        if args.paid is not None:
            args.paid == args.paid == "True"

        if args.bill_type_id is None:
            return "bill_type_id not set", 400
        else:
            billType = models.BillType.query.get(args.bill_type_id)

            if billType is None:
                    return "invalid bill type", 400
            else:
                args.paid = billType.chargeable != True

        bill = models.Bill(amount=args.amount, bill_type_id=args.bill_type_id, notes=args.notes, paid=args.paid, rent_calculation_id=args.rent_calculation_id)

        db.session.add(bill)
        db.session.commit()

        return bill.bill_type_id, 201

class BillAPI(Resource):
    @marshal_with(models.Bill.__json__())
    def get(self, id):
        return models.Bill.query.get(id)

    def put(self, id):
        bill =  models.Bill.query.get(id)
        args = parser.parse_args()

        if args.amount is not None:
            bill.amount = args.amount

        if args.bill_type_id is not None:
            bill.bill_type_id = args.bill_type_id

        if args.notes is not None:
            bill.notes = args.notes

        if args.paid is not None:
            bill.paid = args.paid == "True"

        db.session.commit()
        return

    def delete(self, id):
        bill =  models.Bill.query.get(id)

        db.session.delete(bill)
        db.session.commit()

        return

api.add_resource(BillListAPI, '/bills', endpoint = 'billList')
api.add_resource(BillAPI, '/bills/<int:id>', endpoint = 'bill')