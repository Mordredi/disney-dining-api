from disney_dining.db import db

user_restaurant = db.Table(
    'user_restaurant',
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('user.id'),
        primary_key=True
    ),
    db.Column(
        'restaurant_id',
        db.Integer,
        db.ForeignKey('restaurant.id'),
        primary_key=True
    )
)
