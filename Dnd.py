from flask import Flask
from flask import render_template
from flask import request
from character_creator import create_character
import character

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(name = None):
    return render_template('index.html', name = name)

@app.route('/character', methods=['POST'])
def character():
    # put rolls into an array
    rolls = [
        int(request.form['roll1']),
        int(request.form['roll2']),
        int(request.form['roll3']),
        int(request.form['roll4']),
        int(request.form['roll5']),
        int(request.form['roll6'])
    ]
    # call character_creator with parameters
    character = create_character(request.form['name'], request.form['class'], request.form['race'], rolls)

    # render template with the new character!
    return render_template('character.html', character = character)