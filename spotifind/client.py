import sys
import spotipy
<<<<<<< HEAD
import spotipy.util as util
import pprint
=======
import json

sp = spotipy.Spotify()
>>>>>>> 8bf700a5aa6259f6b82eab91c08ef16f51d664c9

# import spotipy
# import spotipy.oauth2 as oauth2

# credentials = oauth2.SpotifyClientCredentials(
#         client_id=client_id,
#         client_secret=client_secret)
#
# token = credentials.get_access_token()
# spotify = spotipy.Spotify(auth=token)

<<<<<<< HEAD
scope = 'user-top-read'
your_username = 'thepunisherspunishing'
=======
import spotipy.util as util

scope = "user-top-read user-read-private"
your_username = input("Enter your username")
>>>>>>> 8bf700a5aa6259f6b82eab91c08ef16f51d664c9

token = util.prompt_for_user_token(
        username=your_username,
        scope=scope,
        client_id='98e1af2c2aad45ecad9997543623cbbf',
        client_secret='bf63ae87996f4f1aad31335abb361d4e',
<<<<<<< HEAD
        redirect_uri='https://www.getpostman.com/oauth2/callback')

sp = spotipy.Spotify(auth=token)
=======
        redirect_uri='https://localhost:8888/callback/')
>>>>>>> 8bf700a5aa6259f6b82eab91c08ef16f51d664c9

# results = sp.search(q='weezer', limit=20)
# for i, t in enumerate(results['tracks']['items']):
#     print(' ', i, t['name'])

<<<<<<< HEAD
top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
pprint.pprint(top_artists)
=======
if token:
        sp = spotipy.Spotify(auth=token)
        top_artists = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term')
        top_artists_json = json.dumps(top_artists)
        top_artists_json = json.loads(top_artists_json)
        print(top_artists_json)
>>>>>>> 8bf700a5aa6259f6b82eab91c08ef16f51d664c9


# Parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term
# current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

# Parameters:
# limit - the number of entities to return
# offset - the index of the first entity to return
# time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term