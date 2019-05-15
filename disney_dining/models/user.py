from marshmallow import Schema, fields, validate, pre_load
from disney_dining.db import db
from disney_dining.models.user_restaurant import user_restaurant
from disney_dining.models.restaurant import RestaurantSchema


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(87))
    email = db.Column(db.String(80), nullable=False, unique=True)
    restaurants = db.relationship(
        'Restaurant',
        secondary=user_restaurant,
        lazy=False
    )

    def __repr__(self):
        return '<Restaurant %r>' % self.name


class UserSchema(Schema):
    id = fields.Integer()
    firstName = fields.Str()
    lastName = fields.Str()
    password = fields.Str(
        required=True,
        validate=[validate.Length(min=6, max=36)],
        load_only=True,
    )
    email = fields.Str(
        required=True,
        validate=validate.Email(error='Not a valid email address')
    )
    restaurants = fields.Nested(RestaurantSchema, many=True)

    @pre_load
    def process_input(self, data):
        data['email'] = data['email'].lower().strip()
        return data
