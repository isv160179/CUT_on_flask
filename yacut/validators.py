import re

from .constants import (
    WRONG_API_NOT_DATA_IN_REQUEST, PATTERN_LONG_URL, WRONG_URL,
    PATTERN_SHORT_URL, WRONG_CHARS_URL, WRONG_UNIQUE, WRONG_API_NOT_LONG_URL
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


def validate_long_url(data):
    if not data:
        raise InvalidAPIUsage(message=WRONG_API_NOT_DATA_IN_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage(message=WRONG_API_NOT_LONG_URL)
    if not re.match(PATTERN_LONG_URL, data['url']):
        raise InvalidAPIUsage(message=WRONG_URL)


def validate_short_url(data):
    if not re.match(PATTERN_SHORT_URL, data['custom_id']):
        raise InvalidAPIUsage(message=WRONG_CHARS_URL)
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(message=WRONG_UNIQUE)
