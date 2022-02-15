from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Hello", data="Первая страница сайта")


@app.route("/handler", methods=['GET', 'POST'])
def handler():
    if request.method == 'POST':
        return f"<h1>Hello {request.form['name']}</h1>"
    else:
        return redirect(url_for('index'))


@app.route("/profile/<string:name>", methods=['GET', 'POST'])
def profile(name):
    if request.method == 'POST':
#
       return f"<h1>Hello {name}</h1>"
#     else:
#         return redirect(url_for('index'))
    else:
        return f"<h1>Hello {name}</h1>"

