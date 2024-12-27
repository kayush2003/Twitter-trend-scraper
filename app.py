from flask import Flask, render_template, jsonify
import subprocess
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_trends"]
collection = db["trending_topics"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-script")
def run_script():
    try:
        subprocess.run(["python", "twitter_scraper.py"], check=True)
        record = collection.find().sort("end_time", -1).limit(1)[0]
        return jsonify(record)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True,port = 8080)
