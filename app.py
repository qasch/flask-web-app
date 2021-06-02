from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/wow")
def wow():
    return "<h1>nöhö</h1>"