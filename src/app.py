from flask import Flask
from app_library import *
from restplus import config_app, create_app

# configure logger
setup_logging(default_path='logging.json')
logger = logging.getLogger(CONFIG['FLASK']['LOGGER']) # use logger instead of logging
# logger.debug("debug app")
# logger.info("info app")
# logger.warning("warning app")
# logger.error("error app")

# create flask application
app_flask = Flask(__name__)

def main():
    create_app(app_flask, logger)
    app_flask.run(host=CONFIG['FLASK']['HOSTNAME'], port=CONFIG['FLASK']['PORT'], debug=CONFIG['FLASK']['DEBUG'])

if __name__ == "__main__":
    main()