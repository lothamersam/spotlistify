from flask import Blueprint, render_template, abort, redirect, request, session
from jinja2 import TemplateNotFound
from main.services.spotify_service import SpotifyService
from main.factories.service_factory import ServiceFactory

controller = Blueprint('spotify_blueprint', __name__)

spotifyService = ServiceFactory.get_spotify_service()

@controller.route('/auth')
def auth():
    return redirect(spotifyService.build_auth_request_url())

@controller.route('/callback')
def callback():
    auth_token = request.args['code']
    auth_header = spotifyService.authorize(auth_token)

    session['auth_header'] = auth_header

    return redirect('/profile')

@controller.route('/profile')
def user_profile():
    user_data = None
    listening_habits = None

    if 'auth_header' in session:
        user_data = spotifyService.get_user_profile(session['auth_header'])
        listening_habits = spotifyService.get_user_habits(session['auth_header'])

    return render_template('profile_template.html', user=user_data, habits=listening_habits)
    

