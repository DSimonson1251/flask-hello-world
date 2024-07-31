import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from --your name-- in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("your_db_url_here")
    conn.close()
    return "Database connection successful"
