from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello You</h1>"


@app.route("/wow")
def wow():
    return "<h1>nöhö</h1>"