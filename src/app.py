from flask import Flask
from main.blueprints import home_blueprint

app = Flask(__name__)

### BLUEPRINTS ###
app.register_blueprint(home_blueprint.controller)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
