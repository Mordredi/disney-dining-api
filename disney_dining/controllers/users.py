from flask import Blueprint, jsonify, request

from disney_dining.models.user import User, UserSchema
from disney_dining.services.auth import encrypt_password
from disney_dining.services.user import get_user
from disney_dining.db import db

users = Blueprint('users', __name__)

user_schema = UserSchema()


@users.route('/', methods=["POST"])
def create():
    json_data = request.get_json()
    data = user_schema.load(json_data)
    if get_user(data['email']):
        return jsonify({'message': 'User exists'}), 403

    user = User(
        first_name=data['firstName'],
        last_name=data['lastName'],
        email=data['email'],
        password=encrypt_password(data['password'])

    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'})
