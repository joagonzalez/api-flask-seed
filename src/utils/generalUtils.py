import os
import json
import pymsteams
import logging, logging.config
from config.settings import CONFIG

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

def send_teams_message(message):
    """
    Send message to Microsft Teams channel via webhook
    """
    myTeamsMessage = pymsteams.connectorcard(CONFIG['TEAMS']['WEBHOOK_URL'])
    myTeamsMessage.text(message)
    result = myTeamsMessage.send()
    return result
