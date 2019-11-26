import matplotlib.pyplot as plt
import numpy as np


def create_top_genres_pie_chart(genre_data, file_path):
    # Data to plot
    genre_labels = genre_data['top_5_genres_names_list']
    genre_sizes = genre_data['top_5_genres_num_list']

    #colors
    cmap = plt.get_cmap('BuPu')
    colors = [cmap(i) for i in np.linspace(0.1, 0.8, 6)]

    # Plot
    plt.pie(genre_sizes, labels=genre_labels, autopct='%1.1f%%', shadow=True, startangle=140, colors=colors)
    plt.axis('equal')
    plt.title("Top Artist Genres")
    plt.savefig(file_path, transparent=True)
    plt.clf()


def create_live_vs_studio_pie_chart(live_data, file_path):
    live_labels = ["live tracks", "studio tracks"]
    live_sizes = [live_data['num_live'], live_data['num_studio']]

    #colors
    cmap = plt.get_cmap('Blues')
    colors = [cmap(i) for i in np.linspace(0.5, 1, 2)]

    plt.pie(live_sizes, labels=live_labels, autopct='%1.1f%%', shadow=True, startangle=140, colors=colors)
    plt.axis('equal')
    plt.title("Studio vs Live")
    plt.savefig(file_path, transparent=True)
    plt.clf()


def create_acoustic_vs_non_acoustic_pie_chart(acoustic_data, file_path):
    acoustic_labels = ["acoustic tracks", "non-acoustic tracks"]
    acoustic_sizes = [acoustic_data['num_acoustic'], acoustic_data['num_non_acoustic']]

    #colors
    cmap = plt.get_cmap('Purples')
    colors = [cmap(i) for i in np.linspace(0.5, 1, 2)]

    plt.pie(acoustic_sizes, labels=acoustic_labels, autopct='%1.1f%%', shadow=True, startangle=140, colors=colors)
    plt.axis('equal')
    plt.title("Acoustic vs Non-Acoustic")
    plt.savefig(file_path, transparent=True)
    plt.clf()