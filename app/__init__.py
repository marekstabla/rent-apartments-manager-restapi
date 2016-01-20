from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api
from flask.ext.cors import CORS
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
CORS(app)
api = Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models, resources

@app.route('/')
@app.route('/index')
def index():
    return "rent-apartments-manager-restapi"