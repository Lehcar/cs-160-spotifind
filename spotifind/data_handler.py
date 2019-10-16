import json
from spotifind.client import get_token, get_audio_features, get_top_artists, get_top_tracks

your_username = input("Enter your username: ")
scope = "user-top-read"
token = get_token(your_username, scope)

# time_ranges: 'short_term' | 'medium_term' | 'long_term'
time_range = 'short_term'
tracks = get_top_tracks(token, 50, time_range)
items = tracks['items']
track_ids = []
for x in items:
    track_ids.append(x['id'])

print(track_ids)

artists = get_top_artists(token, 50, time_range)

features = get_audio_features(token, track_ids)
