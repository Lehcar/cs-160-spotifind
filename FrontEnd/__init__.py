
from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login_page():
    return render_template('Login.html')


@app.route('/home')
def homepage():
    return render_template('Home.html')


@app.route('/statQuery')
def stat_query():
    return render_template('StatQuery.html')


''' 
Stretch Goals

@app.route('/recs')
def recommendations():
    return render_template('Recommendations.html')


@app.route('/trackAnalysis')
def single_analysis():
    return render_template('TrackAnalysis.html')
'''


if __name__ == '__main__':
    app.run(port=8888, debug=True)
