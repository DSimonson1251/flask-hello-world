from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Daniel Simonson in 3308"
