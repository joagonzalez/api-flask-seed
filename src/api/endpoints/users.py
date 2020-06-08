from flask_restx import Namespace, Api, Resource
from service.LoggerService import loggerService

loggerService.info("initializing namespace with Teams endpoints")

api = Namespace('User Management', description='Endpoints for user management')

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        loggerService.info("alguien entro a hello!")
        return {'hello': 'world'}

