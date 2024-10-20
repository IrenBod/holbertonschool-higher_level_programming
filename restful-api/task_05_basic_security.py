#!/usr/bin/env python3
# Ce script Flask fournit une API sécurisée avec authentification JWT.
# Il inclut des routes protégées nécessitant une authentification utilisateur.


from flask import Flask  # import de la biblioteque framework pour creer les
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
# import de la biblioteque d'autentification
from flask_httpauth import HTTPBasicAuth
# Importation de la fonction pour générer un mot de passe haché
from werkzeug.security import generate_password_hash
# Importation de la fonction pour vérifier si un mot de passe
# correspond à son hachage
from werkzeug.security import check_password_hash

# la creation d'application flask pour creer les decorateurs
app = Flask(__name__)
# La creattion JWT manager
jwt = JWTManager(app)
# la creation d'object d'autentification
auth = HTTPBasicAuth()


users = {
    "user1": generate_password_hash("password1"),
    "admin": generate_password_hash("adminpassword")
}


@auth.verify_password
def verify_password(username, password):
    print(f"Проверка пользователя: {username}, пароль: {password}")
    if (username in users and
            check_password_hash(users.get(username), password)):
        return username
    return None


@app.route("/protected")
@auth.login_required
def protected():
    return "Acces granted!"


app.config["SECRET_KEY"] = "myflasksecretkey"
app.config["JWT_SECRET_KEY"] = "myjwtsecretkey"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if (username not in users or not
            check_password_hash(users[username], password)):
        return jsonify({"msg": "Bad username or passeword"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def protected_route():
    return jsonify(message="JWT Auth: Acces Granted!"), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted!"), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
