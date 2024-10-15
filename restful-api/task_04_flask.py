from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {
    "name": "Jane",
    "age": 28,
    "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_user():
    if request.is_json:

        user_data = request.get_json()

        username = user_data.get("username")
        name = user_data.get("name")
        age = user_data.get("age")
        city = user_data.get("city")

        if not username:
            return jsonify({"error": "Username is required"}), 400

        users[username] = {
            "name": name,
            "age": age,
            "city": city
        }

        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201
    else:
        return jsonify({"error": "REquest must be JSON"}), 400


if __name__ == "__main__":
    app.run()
