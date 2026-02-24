from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

FRONTEND_URL = "https://react-app-xl0h.onrender.com"

CORS(app, origins=[FRONTEND_URL])

@app.route("/")
def hello_world():
    return "<h1>Hello from Flask</h1>"

@app.route("/api/message", methods=["GET"])
def get_message():
    return jsonify(message="Hello from the GET endpoint")

@app.route("/api/message", methods=["POST"])
def post_message():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    return jsonify(response=f"Hello {name}, your POST worked!")
