from app_library import *
from flask import Blueprint
from flask_restx import Api, Resource


blueprint = Blueprint("api version 2", __name__, url_prefix='/api/v2') 
api = Api(blueprint, title='API v2')

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}