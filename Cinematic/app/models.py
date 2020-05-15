from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    dob = db.Column(db.Date())
    cc = db.relationship('CreditCard', backref='owner', lazy='dynamic')
    cart = db.relationship('Cart', backref='user', lazy='dynamic')
    # For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as a
    # convenient way to get access to the "many"

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class CreditCard(db.Model):
    """
    Credit Card Entity
    """
    cc_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    cc_number = db.Column(db.String(16), index=True)
    cc_company = db.Column(db.String(64), index=True)
    cc_expiration = db.Column(db.Date)
    cc_cvc = db.Column(db.Integer)

    def __repr__(self):
        return '<CC {}>'.format(self.cc_id)


class Cart(db.Model):
    """
    Cart Entity
    """
    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True, nullable=False)
    movie_id = db.Column(db.Integer, index=True, nullable=False)
    total_cost = db.Column(db.DECIMAL, nullable=False)

    def __repr__(self):
        return '<Cart {}>'.format(self.movie_id)

