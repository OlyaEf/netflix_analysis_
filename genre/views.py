from flask import Blueprint, jsonify

from genre import utils


genre_bp = Blueprint('genre_bp', __name__)


@genre_bp.route('/<genre>/')
def get_genre_page(genre):
    result = utils.get_genre(genre)
    return jsonify(result)
