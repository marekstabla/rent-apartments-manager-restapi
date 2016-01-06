from flask.ext.restful import Resource, marshal_with
from app import models, api

class ApartmentListAPI(Resource):
    @marshal_with(models.Apartment.__json__())
    def get(self):
        return models.Apartment.query.all()

class ApartmentAPI(Resource):
    @marshal_with(models.Apartment.__json__())
    def get(self, id):
        return models.Apartment.query.get(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(ApartmentListAPI, '/apartments', endpoint = 'apartmentList')
api.add_resource(ApartmentAPI, '/apartments/<int:id>', endpoint = 'apartment')