import json
from flask import Flask, request, redirect, g, render_template
import requests
import data_handler as dh
from urllib.parse import quote

app = Flask(__name__)

#  Client Keys
CLIENT_ID = "98e1af2c2aad45ecad9997543623cbbf"
CLIENT_SECRET = "bf63ae87996f4f1aad31335abb361d4e"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8888
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-top-read"
#can be short_term, medium_term, or long_term
#TODO: take this in from user input
TIME_RANGE = "medium_term"

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
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

    dh.get_data(access_token, TIME_RANGE)

    top_track_names = dh.get_top_track_names()
    top_artist_names = dh.get_top_artist_names()
    top_artist_image = dh.get_top_artist_image()
    top_genres = dh.get_top_genres_data()['top_50_genres_list']

    return render_template('stat-query.html', artists=top_artist_names,
                           tracks=top_track_names, top_artist_image=top_artist_image, genres=top_genres)

if __name__ == "__main__":
    app.run(debug=True, port=PORT)