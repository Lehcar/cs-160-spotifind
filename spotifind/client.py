import spotipy
import spotipy.util as util
import pprint

client_id = '98e1af2c2aad45ecad9997543623cbbf'
client_secret = 'bf63ae87996f4f1aad31335abb361d4e'
redirect_uri='https://localhost:8888/callback/'

def getToken(username, scope):
    token = util.prompt_for_user_token(
        username=username,
        scope=scope,
        client_id= client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)
    return token


# Parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term
def getTopArtists(token, time_range):
    if token:
        sp = spotipy.Spotify(auth=token)
        top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range=time_range)
        pprint.pprint(top_artists)
        return top_artists

scope = "user-top-read user-read-private"
your_username = input("Enter your username: ")
time_range = 'long_term'

token = getToken(your_username, scope)
getTopArtists(token, time_range)