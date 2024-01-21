from flask import Flask, render_template, jsonify
import json
import requests
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World1!"

if __name__ == "__main__":
  app.run(debug=True)
