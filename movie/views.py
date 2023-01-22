from flask import Blueprint, jsonify

from movie import utils


movie_bp = Blueprint('movie', __name__)


@movie_bp.route('/<title>/')
def get_title(title):
    data = utils.get_movie_title(title)
    return jsonify(data)


@movie_bp.route('/<int:from_year>/to/<int:to_year>')
def get_year(from_year, to_year):
    data = utils.get_movie_year(from_year, to_year)
    return jsonify(data)
