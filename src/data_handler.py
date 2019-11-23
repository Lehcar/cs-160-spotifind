import requests
from collections import defaultdict
from collections import OrderedDict
from itertools import islice

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
SPOTIFY_USERS_TOP_ARTISTS = "https://api.spotify.com/v1/me/top/artists"
SPOTIFY_AUDIO_FEATURES = "https://api.spotify.com/v1/audio-features"


def get_data(access_token, time_range):
    track_ids = []
    global top_track_names, top_artist_names, top_genres, live_tracks, studio_tracks, acoustic_tracks,\
        non_acoustic_tracks, top_artist_image
    top_track_names = []
    top_artist_names = []
    top_genres = []
    live_tracks = []
    studio_tracks = []
    acoustic_tracks = []
    non_acoustic_tracks = []
    top_artist_image = None

    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    get_user_top_tracks(authorization_header, time_range, track_ids)
    get_user_top_artists(authorization_header, time_range)
    get_audio_features(authorization_header, track_ids)


def get_user_top_tracks(authorization_header, time_range, track_ids):
    # Get user top tracks
    user_top_tracks_api_endpoint = SPOTIFY_USERS_TOP_TRACKS
    top_track_params = {"limit": "50", "time_range": time_range}
    tracks = requests.get(user_top_tracks_api_endpoint, headers=authorization_header, params=top_track_params).json()
    items = tracks['items']
    for x in items:
        top_track_names.append(x['name'])
        track_ids.append(x['id'])


def get_user_top_artists(authorization_header, time_range):
    user_top_tracks_api_endpoint = SPOTIFY_USERS_TOP_ARTISTS
    top_artist_params = {"limit": "50", "time_range": time_range}
    artists = requests.get(user_top_tracks_api_endpoint, headers=authorization_header, params=top_artist_params).json()
    for artist in artists['items']:
        top_artist_names.append(artist['name'])
        top_genres.append(artist['genres'])
    global top_artist_image
    top_artist_image = artists['items'][0]['images'][0]['url']


def get_audio_features(authorization_header, track_ids):
    tracks = ','.join(map(str, track_ids))
    get_audio_features_api_endpoint = SPOTIFY_AUDIO_FEATURES
    audio_features_params = {"ids": tracks}
    features = requests.get(get_audio_features_api_endpoint, headers=authorization_header,
                            params=audio_features_params).json()
    for track in features['audio_features']:
        if track['liveness'] > 0.8:
            live_tracks.append(track['id'])
        else:
            studio_tracks.append(track['id'])

        if track['acousticness'] > 0.5:
            acoustic_tracks.append(track['id'])
        else:
            non_acoustic_tracks.append(track['id'])


def process_top_genres():
    genre_dict = defaultdict(lambda: 0)
    num_of_genres = 0
    for genre_list in top_genres:
        for genre in genre_list:
            genre_dict[genre] += 1
    ordered_dict = OrderedDict(sorted(genre_dict.items(), key=lambda t: t[1], reverse=True))

    top_5_genres = list(islice(ordered_dict.items(), 5))

    # turn information into json
    num_of_genres = len(genre_dict)
    top_5_genres_names_list = [x[0] for x in top_5_genres]
    top_5_genres_names_list.append("other")
    top_5_genres_num_list = [x[1] for x in top_5_genres]
    num_of_other_genres = num_of_genres - sum(map(lambda x: x, top_5_genres_num_list))
    top_5_genres_num_list.append(num_of_other_genres)
    top_50_genres_list = list(islice(ordered_dict.keys(), 50))
    return {'num_of_genres': num_of_genres, 'top_50_genres_list': top_50_genres_list,
            'top_5_genres_names_list': top_5_genres_names_list, 'top_5_genres_num_list': top_5_genres_num_list}


def get_top_artist_image():
    return top_artist_image


def get_top_track_names():
    return top_track_names


def get_top_artist_names():
    return top_artist_names


def get_top_genres_data():
    return process_top_genres()


def get_live_data():
    return {'live_list': live_tracks, 'studio_list': studio_tracks,
            'num_live': len(live_tracks), 'num_studio': len(studio_tracks)}

def get_acoustic_data():
    return {'acoustic_list': acoustic_tracks, 'non_acoustic_list': non_acoustic_tracks,
            'num_acoustic': len(acoustic_tracks), 'num_non_acoustic': len(non_acoustic_tracks)}
