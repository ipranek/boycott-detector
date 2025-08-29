
from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import flask_cors as CORS
import cv2
import numpy as np
from ultralytics import YOLO
import io

app = Flask(__name__)



DB_PATH = "database/boycott_info.db"

model = YOLO("/Users/ipekoner/Documents/GitHub/boycott-detector/model/my_model-2.pt")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/detect", methods=["POST"])
def detect(): #doing a new detection script bc the og one does it only for testing on local device, not for a server
    file = request.files["frame"].read()
    nparr = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    results = model(img, verbose=False) #running yolo inference without the logs (verbose=False)
    detections = results[0].boxes

    if len(detections) == 0:
        return jsonify({"brand": None})
    

    detected_brands=[]
    for box in detections:
        class_id = int(box.cls.item()) #detect which class ID "x" is (.cls), so gives us a number like # == 2
        brand_name = model.names[class_id] #gives the correspoing label to said number
        detected_brands.append(brand_name)

    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM boycott_info WHERE Brand = ?", (brand_name,)
    ).fetchone()
    conn.close()

    if row:
        return jsonify({
            "brand": row["Brand"],
            "status": row["Boycott_Status"],
            "reason": row["Reason"]
        })
    else: return jsonify({"brand": brand_name, "status": "Unknown", "reason": "Not in database"})


CORS(app, resources={r"/*": {"origins": "*"}}) #"GET" fetches info, "POST" sends the data to the server (process)
@app .route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port = 5001)


