import re

from .constants import (
    WRONG_API_ID_NOT_REQUEST, PATTERN_LONG_URL, WRONG_URL, PATTERN_SHORT_URL,
    WRONG_CHARS_URL, WRONG_UNIQUE
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


def validate_long_url(url):
    if not url:
        raise InvalidAPIUsage(message=WRONG_API_ID_NOT_REQUEST)
    if not re.match(PATTERN_LONG_URL, url):
        raise InvalidAPIUsage(message=WRONG_URL)


def validate_short_url(url):
    if not re.match(PATTERN_SHORT_URL, url):
        raise InvalidAPIUsage(message=WRONG_CHARS_URL)
    if URLMap.query.filter_by(short=url.first()):
        raise InvalidAPIUsage(message=WRONG_UNIQUE)
