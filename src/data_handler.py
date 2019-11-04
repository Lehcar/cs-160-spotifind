import json
import requests

track_ids = []
top_track_names = []
top_artist_names = []
top_genres = []
live_tracks = []
studio_tracks = []
acoustic_tracks = []
non_acoustic_tracks = []
top_artist_image = None

# Spotify URLS
SPOTIFY_USERS_TOP_TRACKS = "https://api.spotify.com/v1/me/top/tracks"
SPOTIFY_USERS_TOP_ARTISTS= "https://api.spotify.com/v1/me/top/artists"
SPOTIFY_AUDIO_FEATURES = "https://api.spotify.com/v1/audio-features"


def get_data(access_token, time_range):

    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    # Get user top tracks
    user_top_tracks_api_endpoint = SPOTIFY_USERS_TOP_TRACKS
    top_track_params = {"limit": "50", "time_range": time_range}
    tracks = requests.get(user_top_tracks_api_endpoint, headers=authorization_header, params=top_track_params).json()
    items = tracks['items']
    for x in items:
        top_track_names.append(x['name'])
        track_ids.append(x['id'])

    user_top_tracks_api_endpoint = SPOTIFY_USERS_TOP_ARTISTS
    top_artist_params = {"limit": "50", "time_range": time_range}
    artists = requests.get(user_top_tracks_api_endpoint, headers=authorization_header, params=top_artist_params).json()
    for artist in artists['items']:
        top_artist_names.append(artist['name'])
        top_genres.append(artist['genres'])
    global top_artist_image
    top_artist_image = artists['items'][0]['images'][0]['url']

    get_audio_features_api_endpoint = SPOTIFY_AUDIO_FEATURES
    audio_features_params = {"ids": track_ids}
    features = requests.get(get_audio_features_api_endpoint, headers=authorization_header, params=audio_features_params).json()

    for track in features['audio_features']:
        if track['liveness'] > 0.8:
            live_tracks.append(track['id'])
        else:
            studio_tracks.append(track['id'])
        if track['acousticness'] > 0.5:
            acoustic_tracks.append(track['id'])
        else:
            non_acoustic_tracks.append(track['id'])


def get_top_artist_image():
    return top_artist_image


def get_top_track_names():
    return top_track_names


def get_top_artist_names():
    return top_artist_names


def get_top_genres_list():
    return top_genres


def get_live_track_list():
    return live_tracks


def get_studio_track_list():
    return studio_tracks


def get_percentage_live():
    return str((len(get_live_track_list()) / (len(get_live_track_list()) + len(get_studio_track_list()))) * 100) + "%"


def get_acoustic_track_list():
    return acoustic_tracks


def get_non_acoustic_track_list():
    return non_acoustic_tracks


def get_percentage_acoustic():
    return str((len(get_acoustic_track_list()) / (len(get_acoustic_track_list()) + len(get_non_acoustic_track_list()))) * 100) + "%"