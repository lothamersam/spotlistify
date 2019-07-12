from flask import Flask
from main.blueprints import home_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint.controller)
