from app_library import *
from flask import Blueprint
from flask_restx import Api, Resource

# set logger config for this blueprint
setup_logging()
logger = logging.getLogger('app_debug') # use logger instead of logging
logger.debug("debug v2")
logger.info("info v2")
logger.warning("warning v2")
logger.error("error v2")

blueprint = Blueprint("api version 2", __name__, url_prefix='/api/v2') 
api = Api(blueprint, title='API v2')

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}