from flask.ext.restful import Resource, marshal_with
from app import models, api

class UserListAPI(Resource):
    @marshal_with(models.User.__json__())
    def get(self):
        return models.User.query.all()

class UserAPI(Resource):
    @marshal_with(models.User.__json__())
    def get(self, id):
        return models.User.query.get(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(UserListAPI, '/users', endpoint = 'userList')
api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')