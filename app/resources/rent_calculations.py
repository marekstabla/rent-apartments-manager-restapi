from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('apartment_id')
parser.add_argument('notes')

class RentCalculationListAPI(Resource):
    @marshal_with(models.RentCalculation.__json__())
    def get(self):
        rent_calculations = models.RentCalculation.query.order_by(models.RentCalculation.id.desc()).all()

        for rent_calculation in rent_calculations:
            rent_calculation.billsPaid = models.Bill.query.filter_by(rent_calculation_id=rent_calculation.id).filter_by(paid=False).count() == 0
            rent_calculation.chargesPaid = models.Charge.query.filter_by(rent_calculation_id=rent_calculation.id).filter_by(paid=False).count() == 0

        return rent_calculations

    def post(self):
        args = parser.parse_args()

        if args.apartment_id is None:
            return "apartment_id not set", 400

        rentCalculation = models.RentCalculation(apartment_id=args.apartment_id, notes=args.notes)

        db.session.add(rentCalculation)
        db.session.commit()

        return rentCalculation.id, 201

class RentCalculationAPI(Resource):
    @marshal_with(models.RentCalculation.__json__())
    def get(self, id):
        return models.RentCalculation.query.get(id)

    def put(self, id):
        rentCalculation =  models.RentCalculation.query.get(id)
        args = parser.parse_args()

        if args.apartment_id is not None:
            rentCalculation.apartment_id = args.apartment_id

        if args.notes is not None:
            rentCalculation.notes = args.notes

        db.session.commit()
        return

    def delete(self, id):
        rentCalculation =  models.RentCalculation.query.get(id)

        db.session.delete(rentCalculation)
        db.session.commit()

        return

api.add_resource(RentCalculationListAPI, '/rent_calculations', endpoint = 'rentCalculationList')
api.add_resource(RentCalculationAPI, '/rent_calculations/<int:id>', endpoint = 'rentCalculation')