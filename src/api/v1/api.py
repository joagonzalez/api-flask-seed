from app_library import *
from flask import Blueprint
from flask_restx import Api, Resource

# set logger config for this blueprint
setup_logging()
logger = logging.getLogger(CONFIG['FLASK']['LOGGER']) # use logger instead of logging
logger.debug("debug v1")
logger.info("info v1")
logger.warning("warning v1")
logger.error("error v1")

blueprint = Blueprint("api version 1", __name__, url_prefix='/api/v1') 
api = Api(blueprint, title='API v1')

# api endpoints
@api.route('/hello')
class Hello(Resource):
    def get(self):
        logger.info("alguien entro a hello!")
        return {'hello': 'world'}