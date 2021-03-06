from flask.ext.restful import Resource, marshal_with, reqparse
from flask import jsonify
from app import models, api, db

parser = reqparse.RequestParser()
parser.add_argument('firstName')
parser.add_argument('lastName')
parser.add_argument('email')
parser.add_argument('telephoneNumber')
parser.add_argument('room_id')

class UserBalanceAPI(Resource):
    def get(self, id):
        user = models.User.query.get(id)
        charges = models.Charge.query.filter_by(paid=False).filter_by(user_id=user.id)

        balance = 0
        for charge in charges:
            if charge.bills is not None:
                 balance += charge.bills
            if charge.rent is not None:
                 balance += charge.rent

        return balance

class UserListAPI(Resource):
    @marshal_with(models.User.__json__())
    def get(self):
        users = models.User.query.all()

        for user in users:
            charges = models.Charge.query.filter_by(paid=False).filter_by(user_id=user.id)

            user.balance = 0
            for charge in charges:
                if charge.bills is not None:
                     user.balance += charge.bills
                if charge.rent is not None:
                     user.balance += charge.rent

        return users;
        
    def post(self):
        args = parser.parse_args()

        if args.firstName is None:
            return "firstName not set", 400

        if args.lastName is None:
            return "lastName not set", 400

        if args.email is None:
            return "email not set", 400

        if args.room_id is not None:
            if args.room_id != "0":
                if models.Room.query.get(args.room_id) is None:
                    return "invalid room"
            else:
                args.rom_id = None

        user = models.User(firstName=args.firstName, lastName=args.lastName, email=args.email, telephoneNumber=args.telephoneNumber, room_id=args.room_id)

        db.session.add(user)
        db.session.commit()

        return user.id, 201

class UserAPI(Resource):
    @marshal_with(models.User.__json__())
    def get(self, id):
        user = models.User.query.get(id)
        charges = models.Charge.query.filter_by(paid=False).filter_by(user_id=user.id)

        user.balance = 0
        for charge in charges:
            if charge.bills is not None:
                 user.balance += charge.bills
            if charge.rent is not None:
                 user.balance += charge.rent

        return user

    def put(self, id):
        user =  models.User.query.get(id)
        args = parser.parse_args()

        if args.firstName is not None:
            user.firstName = args.firstName

        if args.lastName is not None:
            user.lastName = args.lastName

        if args.email is not None:
            user.email = args.email

        if args.telephoneNumber is not None:
            user.telephoneNumber = args.telephoneNumber

        if args.room_id is not None:
            if args.room_id != "0":
                if models.Room.query.get(args.room_id) is None:
                    return "invalid room", 400
                else:
                    user.room_id = args.room_id
            else:
                user.room_id = None


        db.session.commit()
        return

    def delete(self, id):
        user =  models.User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return

api.add_resource(UserListAPI, '/users', endpoint = 'userList')
api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')
api.add_resource(UserBalanceAPI, '/usersBalance/<int:id>', endpoint = 'userBalance')