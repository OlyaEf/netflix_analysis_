from flask import Blueprint, jsonify

from rating import utils


rating_bp = Blueprint('rating_bp', __name__)


@rating_bp.route('/<group>/')
def get_group_page(group):
    rating = utils.get_rating(group)
    result = utils.get_rating_query(rating)
    return jsonify(result)
