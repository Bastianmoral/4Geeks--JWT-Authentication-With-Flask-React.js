"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
import re
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        response_body = { 
            "message": "Access Denied. Check your information"
        }
        return  jsonify(response_body), 400
    if user:
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)


@api.route("/register", methods=["POST"])
def handle_register():
    body = request.get_json()
    new_user = User(
        email = body['email'],
        password = generate_password_hash(body['password'], method='sha256'),
        )
    email = body['email']
    user = User.query.filter_by(email=email).first()
    if user: 
        response_body = {
        "message": "Email already exists",
        }
        return jsonify(response_body), 400
    try:
        password = body['password']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if mat: 
            db.session.add(new_user)
            db.session.commit()
            response_body = {
            "message": "POST users successfully response. Valid password ",
            }
        if not mat:
            response_body = {
            "message": "Invalid Password. it should have at least 6 characters, one Uppercase letter, numbers and one of these symbols: $ @ # %"
            }
            return jsonify(response_body), 400
    except:
        return "An error occurs adding user...", 400

    response_body = {
        "message": "User was created "
    }

    return jsonify(response_body), 200

@api.route("/users", methods=["GET"])
def handle_getusers():
    query_users = Users.query.all()
    query_users = list(map(lambda x: x.serialize(), query_users))
    response_body = {
        "message": "GET users response",
        "users": query_users
    }        

    return jsonify(response_body), 200

@api.route("/users/<int:id>", methods=["DELETE"])
def deleteUser(id):
    user_delete = User.query.get(id)
    if not user_delete:
        response_body = {
            "message": "DELETE /user response ",
            "user": "User not Found"
        }
        return jsonify(response_body), 200        
    db.session.delete(user_delete)
    db.session.commit()
    response_body = {
        "message": "DELETE /user response ",
        "user": "User deleted"
    }
    return jsonify(response_body), 200


@api.route("/hello", methods=["GET"])
@jwt_required()
def get_hello():

    body = {
        "message": "hello world" + email
    }

    return jsonify(body)

