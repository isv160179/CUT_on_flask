from datetime import datetime

from settings import SHORT_URL_LENGHT
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(SHORT_URL_LENGHT), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
