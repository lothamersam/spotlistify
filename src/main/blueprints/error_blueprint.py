from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

controller = Blueprint('error_blueprint', __name__)

@controller.app_errorhandler(404)
def show_404(e):
    return render_template('error/404_error_template.html')

@controller.app_errorhandler(500)
def show_500(e):
    return render_template('error/500_error_template.html')