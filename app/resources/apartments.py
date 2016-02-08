from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('location')

class ApartmentListAPI(Resource):
    @marshal_with(models.Apartment.__json__())
    def get(self):
        apartments = models.Apartment.query.all()

        for apartment in apartments:
            for room in apartment.rooms:
                for user in room.tenants:
                        charges = models.Charge.query.filter_by(paid=False).filter_by(user_id=user.id)
                        user.lastName = user.lastName # no idea why, but this helps
                        user.balance = 0
                        for charge in charges:
                            if charge.bills is not None:
                                 user.balance += charge.bills
                            if charge.rent is not None:
                                 user.balance += charge.rent

        return apartments

    def post(self):
        args = parser.parse_args()

        if args.location is None:
            return "location not set", 400

        newApartment = models.Apartment(location=args.location)

        db.session.add(newApartment)
        db.session.commit()

        return newApartment.id, 201


class ApartmentAPI(Resource):
    @marshal_with(models.Apartment.__json__())
    def get(self, id):
        apartment = models.Apartment.query.get(id)

        for room in apartment.rooms:
            for user in room.tenants:
                    charges = models.Charge.query.filter_by(paid=False).filter_by(user_id=user.id)
                    user.lastName = user.lastName # no idea why, but this helps
                    user.balance = 0
                    for charge in charges:
                        if charge.bills is not None:
                             user.balance += charge.bills
                        if charge.rent is not None:
                             user.balance += charge.rent

        return apartment

    def put(self, id):
        apartment =  models.Apartment.query.get(id)

        args = parser.parse_args()

        if args.location is not None:
            apartment.location = args.location

        db.session.commit()
        return

    def delete(self, id):
        apartment =  models.Apartment.query.get(id)

        db.session.delete(apartment)
        db.session.commit()

        return

api.add_resource(ApartmentListAPI, '/apartments', endpoint = 'apartmentList')
api.add_resource(ApartmentAPI, '/apartments/<int:id>', endpoint = 'apartment')