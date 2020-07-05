# -*- coding: utf-8 -*-
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/today')
def today():
    return datetime.date.today().strftime("%Y/%m/%d")

if __name__ == "__main__":
    app.run()