import spotipy
import spotipy.util as util
import json

client_id = '98e1af2c2aad45ecad9997543623cbbf'
client_secret = 'bf63ae87996f4f1aad31335abb361d4e'
redirect_uri = 'http://localhost:8888/callback'
scope = "user-top-read user-read-private"

"""Gets authorization token for the user

Args:
    username: Spotify username of the user.
    scope: scope of the auth 

Returns:
    token used for authorization

"""


# def get_token(username, scope):
#     token = util.prompt_for_user_token(
#         username=username,
#         scope=scope,
#         client_id=client_id,
#         client_secret=client_secret,
#         redirect_uri=redirect_uri)
#     return token


"""Gets audio features of multiple tracks

Args:
    token: authorization token
    tracks: one or multiple tracks identified by their Spotify IDs (50 max), a list of track URIs, URLs or IDs,max: 50


Returns:
    audio features for the tracks
    https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/

"""


def get_cached_token():
    ''' Gets a cached auth token
    '''
    token_info = None
    try:
        f = open(".cache-thepunisherspunishing")
        token_info_string = f.read()
        f.close()
        token_info = json.loads(token_info_string)

        # if scopes don't match, then bail
        # if 'scope' not in token_info or not self._is_scope_subset(self.scope, token_info['scope']):
        #     return None
        #
        # if self.is_token_expired(token_info):
        #     token_info = self.refresh_access_token(token_info['refresh_token'])

    except IOError:
        pass
    return token_info


def get_audio_features(tracks):
    token = get_cached_token()['access_token']
    sp = spotipy.Spotify(auth=token)
    audio_features = sp.audio_features(tracks)
    return audio_features


"""Get user's top artists

Args:
    token: authorization token
    time_range: ('short_term', 'medium_term', 'long_term') the user's top artists for specified time range

Returns:
    user's top artists for specified time range
    https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/

"""


def get_top_artists(limit, time_range):
    token = get_cached_token()
    sp = spotipy.Spotify(auth=token)
    # limit - the number of entities to return (max 50)
    # offset - the index of the first entity to return
    top_artists = sp.current_user_top_artists(limit=limit, offset=0, time_range=time_range)
    return top_artists


"""Get user's top tracks

Args:
    token: authorization token
    time_range: ('short_term', 'medium_term', 'long_term') the user's top artists for specified time range

Returns:
    user's top artists for specified time range
    https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/

"""


def get_top_tracks(limit, time_range):
    token = get_cached_token()
    sp = spotipy.Spotify(auth=token)
    # limit - the number of entities to return
    # offset - the index of the first entity to return
    top_tracks = sp.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)
    return top_tracks

# your_username = input("Enter your username: ")
# token = get_token(your_username, scope)

# time_ranges: 'short_term' | 'medium_term' | 'long_term'

# print (get_token("AnthonyTech88", scope))