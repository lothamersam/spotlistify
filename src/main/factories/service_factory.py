from main.services.spotify_service import SpotifyService
from main.services.setlist_service import SetlistService

class ServiceFactory:
    spotifyService = SpotifyService()
    setlistService = SetlistService()

    @staticmethod
    def get_spotify_service():
        return ServiceFactory.spotifyService

    @staticmethod
    def get_setlist_service():
        return ServiceFactory.setlistService