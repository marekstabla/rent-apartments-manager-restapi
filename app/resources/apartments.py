from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('location')

class ApartmentListAPI(Resource):
    @marshal_with(models.Apartment.__json__())
    def get(self):
        return models.Apartment.query.all()

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
        return models.Apartment.query.get(id)

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