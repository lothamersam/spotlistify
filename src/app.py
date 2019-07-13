import os
from flask import Flask
from dotenv import load_dotenv
from os.path import join, dirname
from main.blueprints import error_blueprint
from main.blueprints import home_blueprint
from main.blueprints import spotify_blueprint

app = Flask(__name__, static_folder='static/')

load_dotenv(join(dirname(__file__), '..\.env'))

### BLUEPRINTS ###
app.register_blueprint(home_blueprint.controller)
app.register_blueprint(error_blueprint.controller)
app.register_blueprint(spotify_blueprint.controller)

app.secret_key = os.environ.get('APP_SECRET_KEY') 

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
