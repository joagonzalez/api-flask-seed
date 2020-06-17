from config.settings import CONFIG
from flask import Blueprint
from flask_restx import Api, Resource
from service.LoggerService import loggerService
from api.endpoints.users import api as ns_users

loggerService.info("initializing blueprint api v2")

blueprint = Blueprint("api version 2", __name__, url_prefix='/api/v2') 
api = Api(blueprint, title='API v2', version=CONFIG['RESTX']['VERSION']['V2'])
api.add_namespace(ns_users)
