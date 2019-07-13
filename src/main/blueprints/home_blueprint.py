from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

controller = Blueprint('home_blueprint', __name__)

@controller.route('/')
def show_index():
    return render_template('home_template.html')