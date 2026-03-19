from flask import Flask, request, jsonify
from chatbot import chatbot_reply
from database import init_db, add_student, validate_user

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return "College AI Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]
    return jsonify({"response": chatbot_reply(msg)})

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    add_student(data["name"], data["email"], data["password"])
    return jsonify({"status": "registered"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = validate_user(data["email"], data["password"])
    return jsonify({"status": "success" if user else "fail"})

if __name__ == "__main__":
    app.run(debug=True)
