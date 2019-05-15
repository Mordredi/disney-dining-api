from flask import Blueprint, jsonify

from disney_dining.models.restaurant import Restaurant, RestaurantSchema

restaurants = Blueprint('restaurants', __name__)

restaurants_schema = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema()


@restaurants.route('/')
def index():
    restaurants = Restaurant.query.all()
    result = restaurants_schema.dump(restaurants)
    return jsonify(result)


@restaurants.route('/<int:id>')
def show(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'message': 'Restaurant could not be found'}), 404
    result = restaurant_schema.dump(restaurant)
    return jsonify(result)
