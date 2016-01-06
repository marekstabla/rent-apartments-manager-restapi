from flask.ext.restful import Resource, marshal_with
from app import models, api

class RoomListAPI(Resource):
    @marshal_with(models.Room.__json__())
    def get(self):
        return models.Room.query.all()

class RoomAPI(Resource):
    @marshal_with(models.Room.__json__())
    def get(self, id):
        return models.Room.query.get(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(RoomListAPI, '/rooms', endpoint = 'roomList')
api.add_resource(RoomAPI, '/rooms/<int:id>', endpoint = 'room')