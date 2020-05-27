from settings import *
# Import blueprints of each app
from api.v1.api import blueprint as v1
from api.v2.api import blueprint as v2


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