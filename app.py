from piskvorky import move as hraj
from flask import render_template
from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        print("post")
        # Failure to return a redirect or render_template
    else:
        return render_template('index.html')


@app.route("/moves", methods=['POST'])
def move():
    content = request.json
    return jsonify({'moves': hraj(content['moves'])})

