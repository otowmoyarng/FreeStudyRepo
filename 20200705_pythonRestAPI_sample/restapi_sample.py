# -*- coding: utf-8 -*-
from flask import Flask
from datetimeutils import DateTimeUtils

app = Flask(__name__)

@app.route('/hello')
def hello() -> str:
    return "Hello World"

@app.route('/today')
def today() -> str:
    return DateTimeUtils.responcedate(0)

@app.route('/tomorrow')
def tomorrow() -> str:
    return DateTimeUtils.responcedate(1)

@app.route('/yesterday')
def yesterday() -> str:
    return DateTimeUtils.responcedate(-1)

if __name__ == "__main__":
    app.run()