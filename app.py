
from flask import Flask, render_template, jsonify
import sqlite3
import pandas as pd
import flask_cors as CORS

app = Flask(__name__)

DB_PATH = "database/boycott_info.db"

def get_db_connection():
    conn = sqlite3.connect("database/boycott_info.db")
    conn.row_factory = sqlite3.Row
    return conn

CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"]) 
@app .route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port = 5001)


