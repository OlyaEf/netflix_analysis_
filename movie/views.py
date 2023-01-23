from flask import Blueprint, jsonify

from movie import utils


movie_bp = Blueprint('movie', __name__)


@movie_bp.route('/<title>/')
def get_title(title):
    """
    Вьюшка для маршрута /movie/<title> , которая вывод данные про фильм.
    :param title: название фильма.
    :return: данные про фильм.
    """
    data = utils.get_movie_title(title)
    return jsonify(data)


@movie_bp.route('/<int:from_year>/to/<int:to_year>')
def get_year(from_year, to_year):
    """
    Вьюшка для маршрута /movie/year/to/year, которая выводит список словарей.
    :param from_year: первый год
    :param to_year: второй год.
    :return: список словарей.
    """
    data = utils.get_movie_year(from_year, to_year)
    return jsonify(data)
