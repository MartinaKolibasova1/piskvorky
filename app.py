from piskvorky import move as hraj
from flask import render_template
from flask import Flask, request
import os
from piskvorky import Board
from flask.json import jsonify
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'


t = None


@app.route("/", methods=['GET', 'POST'])
def run():
    session['moves'] = []

    if request.method == 'POST':
        print("post")
        # Failure to return a redirect or render_template
    else:
        return redirect(url_for('play'))


@app.route("/hraj", methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        print("post")
        # Failure to return a redirect or render_template
    else:
        return render_template('index.html')


@app.route("/moves", methods=['GET', 'POST'])
def move():
    content = request.json
    print(content)
    return jsonify({'moves': hraj(content['moves'], content['values'])})


if __name__ == "__main__":
    app.run(port=80)
