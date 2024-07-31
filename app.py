import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from --your name-- in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flaskhw3308_user:OS9wVypgEl9Za8I6Pejbn6WVVh3Z9hmT@dpg-cqlabo1u0jms73899qag-a/flaskhw3308")
    conn.close()
    return "Database connection successful"
