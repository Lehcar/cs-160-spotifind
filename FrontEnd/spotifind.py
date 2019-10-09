from flask import Flask, render_template
app = Flask(__name__)


@app.route('/home')
def homepage():
    return render_template('Home.html')


@app.route('/')
@app.route('/login')
def login_page():
    return render_template('Login.html')


if __name__ == '__main__':
    app.run(port=8888, debug=True)
