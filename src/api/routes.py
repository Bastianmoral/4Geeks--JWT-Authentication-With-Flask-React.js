"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route('/register', methods=['POST'])
def register_user():
        response_body_User = request.get_json()
        print(response_body_User)
        if response_body_User is None:
            raise APIException(
                "You need to specify the request body as a json object", status_code=400)
        if 'first_name' not in response_body_User:
            raise APIException(
                'You need to specify your first_name', status_code=400)
        if 'last_name' not in response_body_User:
            raise APIException(
                'You need to specify your last_name', status_code=400)
        if 'email' not in response_body_User:
            raise APIException(
                'You need to specify an email', status_code=400)
        if 'password' not in response_body_User:
            raise APIException(
                'You need to specify a password', status_code=400)

        register_user =  User.query.all()      
        print(register_user)  
        new_user = User(first_name=response_body_User['first_name'],
                        last_name=response_body_User['last_name'],
                        email=response_body_User['email'],
                        password=bcrypt.generate_password_hash(response_body_User['password']).decode())
        db.session.add(new_user)
        db.session.commit()
        serialized_register_user = map(lambda user: user.serialize, register_user)
        print(serialized_register_user)
        filtered_users = list(filter(lambda user: user['first_name'] == response_body_User['first_name'], serialized_register_user))
        return {"User": list(filtered_users), "Everything in it's Right Place": 200}




@api.route("/hello", methods=["GET"])
@jwt_required()
def get_hello():

    dictionary = {
        "message": "hello world"
    }

    return jsonify(dictionary)

