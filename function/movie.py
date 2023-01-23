import sqlite3
import json


def get_movie_title(types, release_year, listed_in):
    """
    Функция, с помощью которой можно будет передавать тип картины (фильм или сериал),
    год выпуска и ее жанр и получать на выходе список названий картин с их описаниями в JSON.
    :return: список названий картин с их описаниями.
    """
    with sqlite3.connect('../netflix.db') as conn:
        cursor = conn.cursor()
        # Фильтрация по результатам агрегации и группировки.
        query = f"""
            SELECT title, description
            FROM netflix
            WHERE type LIKE '%{types}%'
            AND release_year = {release_year}
            AND listed_in LIKE '%{listed_in}%'
            
        """
        result = []
        cursor.execute(query)
        for data in cursor.fetchall():
            result_dict = {
                "title": data[0].strip('\n'),
                "description": data[1].strip('\n')
            }
            result.append(result_dict)
        return result


def movie_to_json(movie):
    """
     Функция записывает список названий картин с их описаниями в JSON.
    :param movie: данные фильма.
    :return: список с описаниями в JSON.
    """
    with open('movies.json', 'w', encoding='utf-8') as f:
        json.dump(movie, f)
    return 'Данные загружены'


movies = get_movie_title('movie', '1990', 'dramas')
data_movie = movie_to_json(movies)

print(data_movie)
