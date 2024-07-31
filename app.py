import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Daniel Simonson in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flaskhw3308_user:OS9wVypgEl9Za8I6Pejbn6WVVh3Z9hmT@dpg-cqlabo1u0jms73899qag-a/flaskhw3308")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://flaskhw3308_user:OS9wVypgEl9Za8I6Pejbn6WVVh3Z9hmT@dpg-cqlabo1u0jms73899qag-a/flaskhw3308")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Create"