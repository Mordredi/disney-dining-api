import requests
import click
from flask.cli import with_appcontext
import simplejson as json
from disney_dining.models.restaurant import Restaurant
from disney_dining.db import db


@click.command('load_restaurants')
@with_appcontext
@click.argument('name')
def load_restaurants(name):
    r = requests.get(f'https://touringplans.com/{name}/dining.json')
    rest = json.loads(r.text)[0]
    for restaurant in rest:
        new = Restaurant(
            name=restaurant['name'],
            category=restaurant['category_code'],
            cuisine=restaurant['cuisine'],
            location=name
        )
        db.session.add(new)
    db.session.commit()
