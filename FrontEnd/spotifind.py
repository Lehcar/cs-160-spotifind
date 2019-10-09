from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login_page():
    return 'Click Here to log in!'


if __name__ == '__main__':
    app.run(debug=True)
