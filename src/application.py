from flask import Flask
from config.settings import CONFIG
from api.v1.api import blueprint as v1
from api.v2.api import blueprint as v2

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.create_app()

    def message(self):
        print("""
  ______ _           _                  _____ _____ 
 |  ____| |         | |           /\   |  __ \_   _|
 | |__  | | __ _ ___| | ________ /  \  | |__) || |  
 |  __| | |/ _` / __| |/ /______/ /\ \ |  ___/ | |  
 | |    | | (_| \__ \   <      / ____ \| |    _| |_ 
 |_|    |_|\__,_|___/_|\_\    /_/    \_\_|   |_____|
                       
        """)

    def config_app(self):
        """
        Configure all the parameters required by Flask App
        """
        self.app.config['SWAGGER_UI_DOC_EXPANSION'] = CONFIG['RESTX']['RESTPLUS_SWAGGER_UI_DOC_EXPANSION']
        self.app.config['RESTPLUS_VALIDATE'] = CONFIG['RESTX']['RESTPLUS_VALIDATE']
        self.app.config['RESTPLUS_MASK_SWAGGER'] = CONFIG['RESTX']['RESTPLUS_MASK_SWAGGER']
        self.app.config['ERROR_404_HELP'] = CONFIG['RESTX']['RESTPLUS_ERROR_404_HELP']

    def create_app(self):  
        """
        Flask app bootstrap
        """  
        self.config_app()
        self.app.register_blueprint(v1)
        self.app.register_blueprint(v2)
    
    def run(self):
        self.message()
        self.app.run(host=CONFIG['FLASK']['HOSTNAME'], port=CONFIG['FLASK']['PORT'], debug=CONFIG['FLASK']['DEBUG'])
