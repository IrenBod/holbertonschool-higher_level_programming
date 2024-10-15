#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)


users = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_users(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_users():
    data = request.get_json()
    if username:
        username = data.get("username")
        name = data.get("name")
        age = data.get("age")
        city = data.get("city")

        users[username] = {"username": username, "name": name, "age": age, "city": city}
        return jsonify({"message": "User added", "user": users[username]}), 201
    else:
        return jsonify({"error": "Missing information"}), 400


if __name__ == "__main__":
    app.run(port=5000)
