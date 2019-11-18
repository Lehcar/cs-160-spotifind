import json
from flask import Flask, request, redirect, g, render_template
import requests
import data_handler as dh
from urllib.parse import quote
import visualizations as viz

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
TIME_RANGE = "short_term"
auth_token = None
post_request = None

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
    global TIME_RANGE
    # Auth Step 1: Authorization
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)

@app.route("/query")
def querypage():
    render_template('stat-query.html');


@app.route("/callback")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    global auth_token, post_request

    #check to see if we already received authorization
    if auth_token == None:
        auth_token = request.args['code']
        code_payload = {
            "grant_type": "authorization_code",
            "code": str(auth_token),
            "redirect_uri": REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
    if post_request == None:
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
    genres_data = dh.get_top_genres_data()

    viz.create_top_genres_pie_chart(genres_data)
    viz.create_acoustic_vs_non_acoustic_pie_chart(dh.get_acoustic_data())
    viz.create_live_vs_studio_pie_chart(dh.get_live_data())

    top_genres = genres_data['top_50_genres_list']

    return render_template('stat-query.html', artists=top_artist_names,
                           tracks=top_track_names, top_artist_image=top_artist_image, genres=top_genres)


@app.route("/callback", methods=['GET', 'POST'])
def change_time_frame():
    global TIME_RANGE # used to access the global TIME_RANGE value
    if request.method == 'POST':
        TIME_RANGE = request.form.get('time_range')

    return index()


if __name__ == "__main__":
    app.run(debug=True, port=PORT)