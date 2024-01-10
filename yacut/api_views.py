from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import WRONG_API_ID_NOT_FOUND
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .validators import validate_long_url, validate_short_url
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    validate_long_url(data)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    else:
        validate_short_url(data)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_link = URLMap.query.filter_by(short=short_id).first()
    if url_link is not None:
        return jsonify({'url': url_link.original}), HTTPStatus.OK
    raise InvalidAPIUsage(
        message=WRONG_API_ID_NOT_FOUND,
        status_code=HTTPStatus.NOT_FOUND
    )
