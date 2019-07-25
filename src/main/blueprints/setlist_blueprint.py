from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

controller = Blueprint('setlist_blueprint', __name__)

@controller.route('/search/<query>')
def show_index(query):
    return render_template('home_template.html')
