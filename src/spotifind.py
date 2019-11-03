import json
from flask import Flask, request, redirect, g, render_template
import requests
from urllib.parse import quote

# Authentication Steps, paramaters, and responses are defined at https://developer.spotify.com/web-api/authorization-guide/
# Visit this url to see all the steps, parameters, and expected response.


app = Flask(__name__)

#  Client Keys
CLIENT_ID = "98e1af2c2aad45ecad9997543623cbbf"
CLIENT_SECRET = "bf63ae87996f4f1aad31335abb361d4e"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8888
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "playlist-modify-public playlist-modify-private user-top-read"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

@app.route('/')
@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route("/home")
def index():
    # Auth Step 1: Authorization
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@app.route("/callback")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    # Get profile data
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    # Get user playlist data
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    playlist_data = json.loads(playlists_response.text)

    #Get user top tracks
    user_top_tracks_api_endpoint ="https://api.spotify.com/v1/me/top/tracks"
    top_track_params = {"limit": "50", "time_range": "long_term"}
    tracks = requests.get(user_top_tracks_api_endpoint, headers=authorization_header, params=top_track_params).json()
    top_track_names = []
    items = tracks['items']
    for x in items:
        top_track_names.append(x['name'])
        #track_ids.append(x['id'])

    user_top_tracks_api_endpoint ="https://api.spotify.com/v1/me/top/artists"
    top_artist_params = {"limit": "50", "time_range": "long_term"}
    artists = requests.get(user_top_tracks_api_endpoint, headers=authorization_header, params=top_artist_params).json()
    top_artist_names = []
    top_genres = []
    #artist_images = None
    for artist in artists['items']:
        top_artist_names.append(artist['name'])
        top_genres.append(artist['genres'])
        #artist_images.append(artist['images'][0]['url'])
    top_artist_image = artists['items'][0]['images'][0]['url']

    return render_template('stat-query.html', artists=top_artist_names,
                           tracks=top_track_names, top_artist_image=top_artist_image)


if __name__ == "__main__":
    app.run(debug=True, port=PORT)