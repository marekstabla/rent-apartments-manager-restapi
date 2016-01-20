from flask.ext.restful import Resource, marshal_with, reqparse
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('apartment_id')

class RoomListAPI(Resource):
    @marshal_with(models.Room.__json__())
    def get(self):
        return models.Room.query.all()

    def post(self):
        args = parser.parse_args()

        if args.apartment_id is None:
            return "apartment_id not set", 400

        if args.name is None:
            return "name not set", 400

        room = models.Room(name=args.name, apartment_id=args.apartment_id)

        db.session.add(room)
        db.session.commit()

        return room.id

class RoomAPI(Resource):
    @marshal_with(models.Room.__json__())
    def get(self, id):
        return models.Room.query.get(id)

    def put(self, id):
        room =  models.Room.query.get(id)
        args = parser.parse_args()

        if args.apartment_id is None:
            return "apartment_id not set", 400

        if args.name is None:
            return "name not set", 400

        room.name = args.name
        room.apartment_id = args.apartment_id

        db.session.commit()
        return

    def delete(self, id):
        room =  models.Room.query.get(id)

        db.session.delete(room)
        db.session.commit()

        return

api.add_resource(RoomListAPI, '/rooms', endpoint = 'roomList')
api.add_resource(RoomAPI, '/rooms/<int:id>', endpoint = 'room')