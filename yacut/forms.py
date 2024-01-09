from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import (
    Length, DataRequired, URL, Optional, Regexp, ValidationError
)

from settings import (
    ORIGINAL_URL_MIN_LENGHT, ORIGINAL_URL_MAX_LENGHT, SHORT_URL_MIN_LENGHT,
    SHORT_URL_MAX_LENGHT, WRONG_LENGTH, WRONG_BLANK, WRONG_URL,
    PATTERN_SHORT_URL, WRONG_CHARS, WRONG_UNIQUE
)
from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField(
        label='Оригинальная ссылка',
        validators=[
            Length(
                min=ORIGINAL_URL_MIN_LENGHT,
                max=ORIGINAL_URL_MAX_LENGHT,
                message=WRONG_LENGTH
            ),
            DataRequired(message=WRONG_BLANK),
            URL(require_tld=True, message=WRONG_URL)
        ]
    )
    custom_id = URLField(
        label='Пользовательский вариант короткой ссылки',
        validators=[
            Length(
                SHORT_URL_MIN_LENGHT,
                SHORT_URL_MAX_LENGHT,
                WRONG_LENGTH
            ),
            Optional(),
            Regexp(PATTERN_SHORT_URL, message=WRONG_CHARS)
        ]
    )
    submit = SubmitField('Создать короткую ссылку.')

    def validate_custom_id(self, custom_id):
        if custom_id.data and URLMap.query.filter_by(
                short=custom_id.data
        ).first():
            raise ValidationError(WRONG_UNIQUE)
