from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    links = db.relationship('Link', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortlink_tag = db.Column(db.Integer, unique=True)
    long_link = db.Column(db.TEXT)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class LinkSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.TEXT)
    link_id = db.Column(db.Integer, db.ForeignKey("link.id"))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
