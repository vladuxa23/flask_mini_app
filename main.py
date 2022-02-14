from flask import Flask, session

app = Flask(__name__)
app.secret_key = "abracadabra"


@app.route("/")
def index():
    print(session.keys())
    return "<h1>HELLO WORLD</h1>"

