import spotipy
import spotipy.util as util
import pprint

client_id = '98e1af2c2aad45ecad9997543623cbbf'
client_secret = 'bf63ae87996f4f1aad31335abb361d4e'
redirect_uri = 'https://localhost:8888/callback/'


# get authorization token for the user
# Parameters:
# username - Spotify username of the user
# scope - scope of the authorization
def getToken(username, scope):
    token = util.prompt_for_user_token(
        username=username,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)
    return token


# get audio features of all tracks user gives
# Parameters:
# token - authorization token
# tracks - one or multiple tracks identified by their Spotify IDs (50 max)
# audio features parameters:
# tracks - one or multiple tracks identified by their Spotify IDs (50 max)
def getAudioFeatures(token, tracks):
    if token:
        sp = spotipy.Spotify(auth=token)
        audio_features = sp.audio_features(tracks)
        pprint.pprint(audio_features)
        return audio_features


# get top artists for user
# Parameters:
# token - authorization token
# time_range - time range user chooses to get top artist
# top artist parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term
def getTopArtists(token, time_range):
    if token:
        sp = spotipy.Spotify(auth=token)
        top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range=time_range)
        pprint.pprint(top_artists)
        return top_artists


# get top tracks for user
# Parameters:
# token - authorization token
# time_range - time range user chooses to get top tracks
# top track parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term
def getTopTracks(token, time_range):
    if token:
        sp = spotipy.Spotify(auth=token)
        top_tracks = sp.current_user_top_tracks(limit=50, offset=0, time_range=time_range)
        pprint.pprint(top_tracks)
        return top_tracks


your_username = input("Enter your username: ")

scope = "user-top-read user-read-private"
token = getToken(your_username, scope)

# time_ranges: 'short_term' | 'medium_term' | 'long_term'
time_range = 'long_term'

# functions:
# getTopArtists(token, time_range)
# getTopTracks(token, time_range)
# getAudioFeatures(token, '3FoiMgXMrO3D5FeJuotKyZ')
