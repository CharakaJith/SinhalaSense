import os
from flask import Flask
from dotenv import load_dotenv
from routes import register_blueprints
from constants.appConstants import app_envs

app = Flask(__name__)

# load environment variables
load_dotenv()

# register all blueprints
register_blueprints(app)

if __name__ == '__main__':
    ENV = os.environ.get('ENV', app_envs.DEV)
    PORT = int(os.environ.get('PORT', 3000))  
    isDebug = ENV == app_envs.DEV

    app.run(debug = isDebug, port = PORT)