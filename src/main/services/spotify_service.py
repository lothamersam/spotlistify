import os
import urllib
import json
import requests
import base64

class SpotifyService():
    SPOTIFY_API_URL = 'https://api.spotify.com/v1/{}'

    SPOTIFY_AUTH_URL_BASE = "https://accounts.spotify.com/{}"
    SPOTIFY_AUTH_URL = SPOTIFY_AUTH_URL_BASE.format('authorize')
    SPOTIFY_TOKEN_URL = SPOTIFY_AUTH_URL_BASE.format('api/token')
    
    CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET_ID = os.environ.get('SPOTIFY_CLIENT_SECRET')
    
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    
    SCOPE = "user-read-private playlist-modify-public playlist-modify-private user-read-recently-played user-top-read"
    
    @classmethod
    def build_auth_request_url(self):
        auth_request_params = {
            "response_type": "code",
            "redirect_uri": self.REDIRECT_URI,
            "scope": self.SCOPE,
            # "state": "spotlisty_request",
            "client_id": self.CLIENT_ID
        }

        return "{}/?{}".format(self.SPOTIFY_AUTH_URL, urllib.parse.urlencode(auth_request_params))
    
    @classmethod
    def authorize(self, auth_token):
        token_request_params = {
            "grant_type": "authorization_code",
            "code": str(auth_token),
            "redirect_uri": self.REDIRECT_URI
        }

        base64encoded = base64.b64encode(("{}:{}".format(self.CLIENT_ID, self.CLIENT_SECRET_ID)).encode())
        headers = {"Authorization": "Basic {}".format(base64encoded.decode())}

        post_request = requests.post(self.SPOTIFY_TOKEN_URL, data=token_request_params, headers=headers)
        access_token = json.loads(post_request.text)["access_token"]

        return {"Authorization": "Bearer {}".format(access_token)}

    @classmethod
    def get_user_profile(self, auth_header):
        profile_endpoint = self.SPOTIFY_API_URL.format('me')
        response = requests.get(profile_endpoint, headers=auth_header)
        return response.json()

    @classmethod
    def get_user_habits(self, auth_header):
        track_habits_endpoint = self.SPOTIFY_API_URL.format('me/top/artists')
        response = requests.get(track_habits_endpoint, headers=auth_header)
        return response.json()
        
