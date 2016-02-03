from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('chargeable')
parser.add_argument('should_calculate')

class BillTypeListAPI(Resource):
    @marshal_with(models.BillType.__json__())
    def get(self):
        return models.BillType.query.all()

    def post(self):
        args = parser.parse_args()

        if args.chargeable is None:
            args.chargeable = 0

        if args.should_calculate is None:
            args.should_calculate = 0

        billType = models.BillType(name=args.name, chargeable=args.chargeable, should_calculate=args.should_calculate)

        db.session.add(billType)
        db.session.commit()

        return billType.id, 201

class BillTypeAPI(Resource):
    @marshal_with(models.BillType.__json__())
    def get(self, id):
        return models.BillType.query.get(id)

    def put(self, id):
        billType =  models.BillType.query.get(id)
        args = parser.parse_args()

        if args.name is not None:
            billType.name = args.name

        if args.chargeable is not None:
            billType.chargeable = args.chargeable

        if args.should_calculate is not None:
            billType.should_calculate = args.should_calculate

        db.session.commit()
        return

    def delete(self, id):
        billType =  models.BillType.query.get(id)

        db.session.delete(billType)
        db.session.commit()

        return

api.add_resource(BillTypeListAPI, '/bill_types', endpoint = 'billTypeList')
api.add_resource(BillTypeAPI, '/bill_types/<int:id>', endpoint = 'billType')