
from flask import Flask, render_template, jsonify
import sqlite3
import pandas as pd
import flask_cors as CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"]) 
@app .route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port = 5001)


