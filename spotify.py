from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = os.getenv('REDIRECT_URL')

scope = "user-library-read"

def create_spotify_oauth() :
    return SpotifyOAuth(
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_url,
        scope = scope
    )

def create_spotify_client():
    global sp
    sp = spotipy.Spotify(auth_manager=create_spotify_oauth())

def get_saved_tracks(limit, offset):
    results = sp.current_user_saved_tracks(limit=limit, offset=offset)
    result_list = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        result_list.append(track['artists'][0]['name'] + " " + track['name'])
    return result_list
