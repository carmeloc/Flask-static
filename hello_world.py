#!/usr/bin/env python3
# hello_world.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

