from datetime import datetime

from flask import url_for

from . import db
from .constants import SHORT_URL_MAX_LENGHT


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(SHORT_URL_MAX_LENGHT), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'url': self.original,
            'short_link': url_for(
                'short_view',
                short=self.short,
                _external=True
            )
        }

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
