from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Dank Memes 420 69'