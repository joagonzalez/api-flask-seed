import os
import json
import pymsteams
import logging, logging.config
from settings import *

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
