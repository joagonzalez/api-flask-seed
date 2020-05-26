from flask import Flask, jsonify
from flask_restx import Api, Resource
from app_library import *
from models import *

# configure logger
setup_logging(default_path='logging.json')
logger = logging.getLogger(CONFIG['FLASK']['LOGGER']) # use logger instead of loggin

# congure flask and restx app
app_flask = Flask(__name__)
app = Api(app=app_flask, version=CONFIG['RESTX']['VERSION'], title=CONFIG['RESTX']['TITLE'], description=CONFIG['RESTX']['DESCRIPTION'])

# endpoint models
message_model = app.model('Message model', message_model_definition)

BUFFER = []

# api endpoints
@app.route('/status')
class Status(Resource):
    def get(self):
        """
        Used to check service status
        """
        pass

@app.route('/message')
class Message(Resource):
    def get(self):
        """
        Query messages sent to MS Teams Channel
        """
        result = []
        for msg in BUFFER:
            result.append(msg)

        return result, 201

    @app.expect(message_model)
    def post(self):
        """
        Send a message to a MS Teams Channel
        """
        payload = app.payload
        msg = payload['from'] + ': ' + payload['message']
        try:
            r = send_teams_message(msg)
            BUFFER.append(msg)
        except Exception as e: 
            logging.error("Error trying to send the message!")
            r = e
        
        return r

if __name__ == "__main__":
    create_app(app_flask, logger)