from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pw: str):
        # force PBKDF2+SHA256 instead of scrypt (avoid missing hashlib.scrypt)
        self.password_hash = generate_password_hash(
            pw,
            method="pbkdf2:sha256",
            salt_length=8
        )

    def check_password(self, pw: str) -> bool:
        return check_password_hash(self.password_hash, pw)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))