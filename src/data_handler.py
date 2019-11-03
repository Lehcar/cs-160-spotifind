import json
from src.client import get_audio_features, get_top_artists, get_top_tracks

track_ids = []
top_track_names = []
top_artist_names = []
top_genres = []
live_tracks = []
studio_tracks = []
acoustic_tracks = []
non_acoustic_tracks = []

artist_images = []


def get_data():
    #your_username = input("Enter your username: ")
    # scope = "user-top-read"
    # token = get_token(your_username, scope)
    # time_ranges: 'short_term' | 'medium_term' | 'long_term'
    time_range = 'long_term'
    limit = 50

    tracks = get_top_tracks(limit, time_range)
    items = tracks['items']
    for x in items:
        top_track_names.append(x['name'])
        track_ids.append(x['id'])

    artists = get_top_artists(tlimit, time_range)
    artist_items = artists['items']
    for artist in artist_items:
        top_artist_names.append(artist['name'])
        top_genres.append(artist['genres'])
        artist_images.append(artist['images'][0]['url'])

    features = get_audio_features(track_ids)
    for track in features:
        if track['liveness'] > 0.8:
            live_tracks.append(track['id'])
        else:
            studio_tracks.append(track['id'])
        if track['acousticness'] > 0.5:
            acoustic_tracks.append(track['id'])
        else:
            non_acoustic_tracks.append(track['id'])

def get_top_artist_images():
    return artist_images[0]

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


# top track names, top artist names, top genres, list of top genres names,
# number of studio tracks, number of live tracks