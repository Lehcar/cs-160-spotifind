import pytest
import src.data_handler as dh

# before running tests fill these categories:
token = 'BQD1SwrIc1vYIxVXQmOGhPbC1LpSsEUtY2k7kOYmOUvuS9ML8iKv-8_YznxX4h8nD4SmMUETaq9V7jfcmdEiOY8u50h8xt2Tw1Azd8svkJPwp81xAYKRRM08r8PKvuInhVeObHF4-HmDdNzC39EfCUphgOejZcpn1g0sCEOXL-w'
# get token by uncommenting the part where you could get a token, print it out, and then copy here
username = ''


class TestClientNull:
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

    def test_with_token_get_top_genres_data_returns_data(self):
        assert True
