import spotipy
import spotipy.util as util
import pprint

client_id = '98e1af2c2aad45ecad9997543623cbbf'
client_secret = 'bf63ae87996f4f1aad31335abb361d4e'
redirect_uri = 'https://localhost:8888/callback/'
scope = "user-top-read user-read-private"


"""Gets authorization token for the user

Args:
    username: Spotify username of the user.
    scope: scope of the auth 

Returns:
    token used for authorization

"""
def get_token(username, scope):
    token = util.prompt_for_user_token(
        username=username,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)
    return token


"""Gets audio features of multiple tracks

Args:
    token: authorization token
    tracks: one or multiple tracks identified by their Spotify IDs (50 max)

Returns:
    audio features for the tracks
    https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/

"""
def get_audio_features(token, tracks):
    if token:
        sp = spotipy.Spotify(auth=token)
        audio_features = sp.audio_features(tracks)
        pprint.pprint(audio_features)
        return audio_features


"""Get user's top artists

Args:
    token: authorization token
    time_range: ('short_term', 'medium_term', 'long_term') the user's top artists for specified time range

Returns:
    user's top artists for specified time range
    https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/

"""
def get_top_artists(token, time_range):
    if token:
        sp = spotipy.Spotify(auth=token)
        # limit - the number of entities to return (max 50)
        # offset - the index of the first entity to return
        top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range=time_range)
        pprint.pprint(top_artists)
        return top_artists


"""Get user's top tracks

Args:
    token: authorization token
    time_range: ('short_term', 'medium_term', 'long_term') the user's top artists for specified time range

Returns:
    user's top artists for specified time range
    https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/

"""
def get_top_tracks(token, time_range):
    if token:
        sp = spotipy.Spotify(auth=token)
        # limit - the number of entities to return
        # offset - the index of the first entity to return
        top_tracks = sp.current_user_top_tracks(limit=50, offset=0, time_range=time_range)
        pprint.pprint(top_tracks)
        return top_tracks


your_username = input("Enter your username: ")
token = get_token(your_username, scope)

# time_ranges: 'short_term' | 'medium_term' | 'long_term'
time_range = 'long_term'

