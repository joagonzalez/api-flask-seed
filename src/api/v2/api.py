from utils.generalUtils import *
from flask import Blueprint
from flask_restx import Api, Resource
from service.LoggerService import loggerService

loggerService.info("initializing blueprint api v2")

blueprint = Blueprint("api version 2", __name__, url_prefix='/api/v2') 
api = Api(blueprint, title='API v2')

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}