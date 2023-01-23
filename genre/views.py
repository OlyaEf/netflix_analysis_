from flask import Blueprint, jsonify

from genre import utils


genre_bp = Blueprint('genre_bp', __name__)


@genre_bp.route('/<genre>/')
def get_genre_page(genre):
    """
    Вьюшка `/genre/<genre>` которая возвращает список.
    В результате должно содержаться название и описание каждого фильма.
    :param genre: жанр фильма.
    :return: возвращает список.
    """
    result = utils.get_genre(genre)
    return jsonify(result)
