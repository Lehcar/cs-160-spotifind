import pytest
import src.data_handler as dh

class TestDataHandlerNull:
    def test_no_token_get_data(self):
        with pytest.raises(Exception):
            dh.get_data({}, "short_term")
        assert len(dh.get_top_track_names()) == 0
        with pytest.raises(Exception):
            dh.get_data({}, "medium_term")
        assert len(dh.get_top_artist_names()) == 0
        with pytest.raises(Exception):
            dh.get_data({}, "long_term")
        assert len(dh.get_top_track_names()) == 0

    def test_no_token_get_top_genres_data_returns_empty_list(self):
        with pytest.raises(Exception):
            dh.get_user_top_artists({}, "short_term")
        assert len(dh.get_top_genres_data()['top_50_genres_list']) == 0
        with pytest.raises(Exception):
            dh.get_user_top_artists({}, "medium_term")
        assert len(dh.get_top_genres_data()['top_50_genres_list']) == 0
        with pytest.raises(Exception):
            dh.get_user_top_artists({}, "long_term")
        assert len(dh.get_top_genres_data()['top_50_genres_list']) == 0
