from flask import Flask
from app_library import *
from bootstrap import config_app, create_app

<<<<<<< HEAD
@app.route('/')
def hello():
    return "Hello heroku!!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
=======
# configure logger
setup_logging(default_path='logging.json')
logger = logging.getLogger(CONFIG['FLASK']['LOGGER']) # use logger instead of logging
# logger.debug("debug app")
# logger.info("info app")
# logger.warning("warning app")
# logger.error("error app")

# create flask application
app_flask = Flask(__name__)
>>>>>>> f89ec77128c9cb5ff1441a82e5737f93c0b6569c

def main():
    create_app(app_flask, logger)
    app_flask.run(host=CONFIG['FLASK']['HOSTNAME'], port=CONFIG['FLASK']['PORT'], debug=CONFIG['FLASK']['DEBUG'])

if __name__ == "__main__":
    main()