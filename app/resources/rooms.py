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

        return room.id, 201

class RoomAPI(Resource):
    @marshal_with(models.Room.__json__())
    def get(self, id):
        return models.Room.query.get(id)

    def put(self, id):
        room =  models.Room.query.get(id)
        args = parser.parse_args()

        if args.apartment_id is not None:
            room.apartment_id = args.apartment_id

        if args.name is not None:
            room.name = args.name


        db.session.commit()
        return

    def delete(self, id):
        room =  models.Room.query.get(id)

        if room.tenants.count() > 0:
            return "Can't delete room with tenants", 400

        db.session.delete(room)
        db.session.commit()

        return

api.add_resource(RoomListAPI, '/rooms', endpoint = 'roomList')
api.add_resource(RoomAPI, '/rooms/<int:id>', endpoint = 'room')