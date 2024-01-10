from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import (
    Length, DataRequired, URL, Optional, Regexp, ValidationError
)

from settings import (
    LONG_URL_MIN_LENGHT, LONG_URL_MAX_LENGHT, SHORT_URL_MIN_LENGHT,
    SHORT_URL_MAX_LENGHT, WRONG_LENGTH, WRONG_BLANK, WRONG_URL,
    PATTERN_SHORT_URL, WRONG_CHARS_URL, WRONG_UNIQUE, FORM_LABEL_LONG_URL,
    FORM_LABEL_SHOT_URL, FORM_LABEL_BUTTON_CREATE
)
from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField(
        label=FORM_LABEL_LONG_URL,
        validators=[
            DataRequired(message=WRONG_BLANK),
            URL(require_tld=True, message=WRONG_URL),
            Length(
                min=LONG_URL_MIN_LENGHT,
                max=LONG_URL_MAX_LENGHT,
                message=WRONG_LENGTH
            )
        ]
    )
    custom_id = URLField(
        label=FORM_LABEL_SHOT_URL,
        validators=[
            Optional(),
            Regexp(PATTERN_SHORT_URL, message=WRONG_CHARS_URL),
            Length(
                SHORT_URL_MIN_LENGHT,
                SHORT_URL_MAX_LENGHT,
                WRONG_LENGTH
            )
        ]
    )
    submit = SubmitField(label=FORM_LABEL_BUTTON_CREATE)

    def validate_custom_id(self, custom_id):
        if custom_id.data and URLMap.query.filter_by(
                short=custom_id.data
        ).first():
            raise ValidationError(WRONG_UNIQUE)
