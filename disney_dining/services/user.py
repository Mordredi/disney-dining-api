from sqlalchemy import func
from disney_dining.models.user import User


def get_user(email):
    return User.query.filter(func.lower(User.email) == email.lower()).first()