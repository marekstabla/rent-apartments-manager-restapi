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
    	newApartment = models.Apartment(location=args.location)

    	db.session.add(newApartment)
    	db.session.commit()

    	return newApartment.id


class ApartmentAPI(Resource):
    @marshal_with(models.Apartment.__json__())
    def get(self, id):
        return models.Apartment.query.get(id)

    def put(self, id):
        apartment =  models.Apartment.query.get(id)

        args = parser.parse_args()
        apartment.location = args.location

        db.session.commit()
        pass

    def delete(self, id):
        apartment =  models.Apartment.query.get(id)
        db.session.delete(apartment)
        db.session.commit()
        pass

api.add_resource(ApartmentListAPI, '/apartments', endpoint = 'apartmentList')
api.add_resource(ApartmentAPI, '/apartments/<int:id>', endpoint = 'apartment')