from utils.generalUtils import *
from flask import Blueprint
from flask_restx import Api, Resource
from service.LoggerService import loggerService
from models.message import message_model_definition
loggerService.info("initializing blueprint api v1")

blueprint = Blueprint("api version 1", __name__, url_prefix='/api/v1') 
api = Api(blueprint, title='API v1')

message_model = api.model('Message model', message_model_definition)

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        loggerService.info("alguien entro a hello!")
        return {'hello': 'world'}

@api.route('/sendMessage')
class SendMessage(Resource):
    @api.expect(message_model)
    def post(self):
        loggerService.info("Sending a message to MS Teams")
        message = api.payload
        send_teams_message(message['from'] + ': ' + message['message'])
        return {
            'channel': 'DevOps',
            'organization': 'Newtech',
            'message': message['message'],
            'from': message['from']
            }