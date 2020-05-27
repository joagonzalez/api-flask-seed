import os
import json
import pymsteams
import logging, logging.config
from settings import *
from flask_restx import Api
# Import blueprints of each app
from api.v1.api import blueprint as v1
from api.v2.api import blueprint as v2

# general purpose functions
def open_file(filename):
    """
    Open file function with exceptions treatment
    """
    result = []
    try:
        f = open(filename, 'r')
        for line in f:
            result.append(line)
        f.close()
        return result
    except Exception as e:
        logging.error(e)

def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    Logging loggers and handlers condifuration via logging.json file parameters
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def send_teams_message(message):
    """
    Send message to Microsft Teams channel via webhook
    """
    myTeamsMessage = pymsteams.connectorcard(CONFIG['TEAMS']['WEBHOOK_URL'])
    myTeamsMessage.text(message)
    result = myTeamsMessage.send()
    return result

def config_app(app):
    """
    Configure all the parameters required by Flask App
    """
    app.config['SWAGGER_UI_DOC_EXPANSION'] = CONFIG['RESTX']['RESTPLUS_SWAGGER_UI_DOC_EXPANSION']
    app.config['RESTPLUS_VALIDATE'] = CONFIG['RESTX']['RESTPLUS_VALIDATE']
    app.config['RESTPLUS_MASK_SWAGGER'] = CONFIG['RESTX']['RESTPLUS_MASK_SWAGGER']
    app.config['ERROR_404_HELP'] = CONFIG['RESTX']['RESTPLUS_ERROR_404_HELP']

def create_app(app, logger):  
    """
    Flask app bootstrap
    """  
    config_app(app)

    app.register_blueprint(v1)
    app.register_blueprint(v2)