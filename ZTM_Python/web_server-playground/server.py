import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route("/blog")
def blog():
    return "These are my thoughts on blogs"


@app.route("/blog/2023/dogs")
def blog2():
    return "This is my dog"
