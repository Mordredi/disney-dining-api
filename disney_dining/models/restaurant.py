from marshmallow import Schema, fields
from disney_dining.db import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    cuisine = db.Column(db.String(80))
    location = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Restaurant %r>' % self.name


class RestaurantSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    category = fields.Str()
    cuisine = fields.Str()
    location = fields.Str()
