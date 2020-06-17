from config.settings import CONFIG
from flask import Blueprint
from flask_restx import Api
from service.LoggerService import loggerService
from models.message import message_model_definition, message_card_model, facts_model
from api.endpoints.teams import api as ns_teams
from api.endpoints.users import api as ns_users

loggerService.info("initializing blueprint api v1")

blueprint = Blueprint("api version 1", __name__, url_prefix='/api/v1') 

api = Api(blueprint, title='API v1', version=CONFIG['RESTX']['VERSION']['V1'])
api.add_namespace(ns_teams)
api.add_namespace(ns_users)


