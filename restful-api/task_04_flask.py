#!/usr/bin/python3
"""This module defines basics of susage of Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    if not new_user or "name" not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user["name"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({
            "message": "User added",
            "user": new_user
        }), 201


if __name__ == "__main__":
    app.run()
