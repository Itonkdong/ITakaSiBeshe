from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

with open("static/data.json", "r") as jsonFile:
    DATA = json.load(jsonFile)


@app.route('/')
def getIndex():
    return "Hello World!"



if __name__ == '__main__':
    app.run(debug=True)