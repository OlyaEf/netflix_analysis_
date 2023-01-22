import sqlite3


def get_movie_title(word):
    with sqlite3.connect('./netflix.db') as connection:
        cursor = connection.cursor()
        # Фильтрация по результатам агрегации и группировки.
        try:
            query = f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '{word}' AND type = 'Movie' 
                ORDER BY release_year DESC
            """
            cursor.execute(query)
            results = []
            for data in cursor.fetchall():
                result = {
                    "title": data[0],
                    "country": data[1],
                    "release_year": data[2],
                    "genre": data[3],
                    "description": data[4],
                }
                results.append(result)
            return results[0]
        except IndexError:
            return []


def get_movie_year(from_year, to_year):
    with sqlite3.connect('./netflix.db') as connection:
        cursor = connection.cursor()
        # Фильтрация по результатам агрегации и группировки.
        query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN '{from_year}' AND '{to_year}'
            AND type = 'Movie'
            LIMIT 100
        """
        cursor.execute(query)
        results = []
        for data in cursor.fetchall():
            result = {
                "title": data[0],
                "release_year": data[1],
            }
            results.append(result)
        return results


# print(get_movie_title(21))
# print(get_movie_year('2015', '2020'))
