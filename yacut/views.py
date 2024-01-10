from http import HTTPStatus
from random import choices

from flask import flash, url_for, render_template, redirect

from . import app, db
from .constants import ALLOW_SHORT_URL_CHARS, SHORT_URL_LENGHT
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id(chars=ALLOW_SHORT_URL_CHARS, lenght=SHORT_URL_LENGHT):
    while True:
        unique_short_id = ''.join(choices(chars, k=lenght))
        if not URLMap.query.filter_by(short=unique_short_id).first():
            return unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        flash(url_for('short_view', short=short, _external=True))

    return render_template('index.html', form=form), HTTPStatus.OK


@app.route('/<string:short>')
def short_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
