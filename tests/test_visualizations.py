import pytest
import os
from os import path
import src.visualizations as viz


''' Methods to test: 
    create_top_genres_pie_chart(genre_data)
    create_live_vs_studio_pie_chart(live_data)
    create_acoustic_vs_non_acoustic_pie_chart(acoustic_data)
'''


class TestCharts:

    def test_top_genres_pie_chart(self):
        #remove the old chart
        try:
            os.remove("src/static/genres_pie_chart.png")
        except FileNotFoundError:
            # do nothing
            print("Continue tests")

        #Build sample genre data
        genre_test_data = {'top_5_genres_names_list': ['yodeling', 'death_metal', 'other'],
                           'top_5_genres_num_list': [25, 25, 50]}
        viz.create_top_genres_pie_chart(genre_test_data, "src/static/genres_pie_chart.png")

        #assert the chart is created
        assert path.exists("src/static/genres_pie_chart.png")

    def test_live_vs_studio_pie_chart(self):
        # remove the old chart
        try:
            os.remove("src/static/live_pie_chart.png")
        except FileNotFoundError:
            # do nothing
            print("Continue tests")

        # Build sample genre data
        live_test_data = {'num_live': 50, 'num_studio': 50}
        viz.create_live_vs_studio_pie_chart(live_test_data, "src/static/live_pie_chart.png")

        # assert the chart is created
        assert path.exists("src/static/acoustic_pie_chart.png")
    def test_acoustic_vs_non_acoustic_pie_chart(self):
        # remove the old chart
        try:
            os.remove("src/static/acoustic_pie_chart.png")
        except FileNotFoundError:
            # do nothing
            print("Continue tests")

        # Build sample genre data
        acoustic_test_data = {'num_acoustic': 50, 'num_non_acoustic': 50}
        viz.create_acoustic_vs_non_acoustic_pie_chart(acoustic_test_data, "src/static/acoustic_pie_chart.png")

        # assert the chart is created
        assert path.exists("src/static/acoustic_pie_chart.png")