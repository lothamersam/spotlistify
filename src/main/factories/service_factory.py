from main.services.spotify_service import SpotifyService

class ServiceFactory:

    @staticmethod
    def get_spotify_service():
        return SpotifyService()