from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# define blueprint object for home
controller = Blueprint('home_blueprint', __name__)

### BLUEPRINT ROUTES ###

@controller.route('/')
def show():
    return render_template('home_template.html')