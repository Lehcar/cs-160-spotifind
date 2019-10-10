import spotipy
import spotipy.util as util
import pprint

# import spotipy.oauth2 as oauth2

# credentials = oauth2.SpotifyClientCredentials(
#         client_id=client_id,
#         client_secret=client_secret)
#
# token = credentials.get_access_token()

#scope = 'user-top-read'
#your_username = 'thepunisherspunishing'

scope = "user-top-read user-read-private"
your_username = raw_input("Enter your username: ")

token = util.prompt_for_user_token(
        username=your_username,
        scope=scope,
        client_id='98e1af2c2aad45ecad9997543623cbbf',
        client_secret='bf63ae87996f4f1aad31335abb361d4e',
        redirect_uri='https://www.getpostman.com/oauth2/callback')

sp = spotipy.Spotify(auth=token)
redirect_uri='https://localhost:8888/callback/'

if token:
    sp = spotipy.Spotify(auth=token)
    top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
    pprint.pprint(top_artists)


# Parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term
# current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

# Parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term