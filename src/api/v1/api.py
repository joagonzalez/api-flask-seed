from app_library import *
from flask import Blueprint
from flask_restx import Api, Resource

blueprint = Blueprint("api version 1", __name__, url_prefix='/api/v1') 
api = Api(blueprint, title='API v1')

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}