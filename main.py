from flask import Flask, session, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Hello", data="Первая страница сайта")

