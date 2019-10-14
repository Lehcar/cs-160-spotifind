import pytest

from spotifind.client import get_token, get_audio_features

client_id = '98e1af2c2aad45ecad9997543623cbbf'
client_secret = 'bf63ae87996f4f1aad31335abb361d4e'
redirect_uri = 'https://localhost:8888/callback/'


class TestClient:
    def test_get_token(self):
        username = ''  # have a username
        get_token(username, "user-top-read user-read-private").exists()

    def test_get_audio_features(self):
        username = ''  # have a username
        value = [{'acousticness': 0.0417,
                  'analysis_url': 'https://api.spotify.com/v1/audio-analysis/3FoiMgXMrO3D5FeJuotKyZ',
                  'danceability': 0.596,
                  'duration_ms': 209519,
                  'energy': 0.893,
                  'id': '3FoiMgXMrO3D5FeJuotKyZ',
                  'instrumentalness': 0,
                  'key': 1,
                  'liveness': 0.315,
                  'loudness': -3.43,
                  'mode': 0,
                  'speechiness': 0.16,
                  'tempo': 79.889,
                  'time_signature': 4,
                  'track_href': 'https://api.spotify.com/v1/tracks/3FoiMgXMrO3D5FeJuotKyZ',
                  'type': 'audio_features',
                  'uri': 'spotify:track:3FoiMgXMrO3D5FeJuotKyZ',
                  'valence': 0.526}]
        assert get_audio_features(get_token(username, "user-top-read user-read-private"),
                                  '3FoiMgXMrO3D5FeJuotKyZ') == value
