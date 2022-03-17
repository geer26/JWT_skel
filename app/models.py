import json, uuid
import hashlib
from app import db, jwt
import bcrypt
from datetime import datetime


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


class User(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.Date(), default=datetime.now(), nullable=False)
    last_modified_at = db.Column(db.Date(), default=datetime.now(), nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)
    is_enabled = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<ID: {self.id}> <Username: {self.username}> <Is superuser:{self.is_superuser}>'

    def set_password(self, password):
        hash = hashlib.sha3_512()
        hash.update(password.encode('utf-8'))
        self.password_hash = hash.hexdigest()
        return True

    def check_password(self, password):
        hash = hashlib.sha3_512()
        hash.update(password.encode('utf-8'))
        c_password = hash.hexdigest()
        if c_password == self.password_hash:
            return True
        else:
            return False