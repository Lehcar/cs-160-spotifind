from .client import *

your_username = input("Enter your username: ")
token = get_token(your_username, scope)

# time_ranges: 'short_term' | 'medium_term' | 'long_term'
time_range = 'long_term'
tracks = get_top_tracks(token, time_range)
print(type(tracks))

artists = get_top_artists(token, time_range)
print(type(artists))

# features = get_audio_features(token, tracks)
# print(type(features))

