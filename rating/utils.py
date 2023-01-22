import sqlite3


def get_rating(group):
    if group.lower() == 'children':
        return 'G', 'G'
    elif group.lower() == 'family':
        return 'G', 'PG', 'PG-13'
    elif group.lower() == 'adult':
        return 'R', 'NC-17'
    else:
        return 'Dont know this group'


def get_rating_query(rating):
    with sqlite3.connect('./netflix.db') as connection:
        cursor = connection.cursor()
        # Фильтрация по результатам агрегации и группировки.
        try:
            query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN {rating} AND type = 'Movie' 
            """
            results = []
            cursor.execute(query)
            for data in cursor.fetchall():
                result = {
                    "title": data[0],
                    "rating": data[1],
                    "description": data[2],
                }
                results.append(result)
        except IndexError:
            return []
        return results


# print(get_rating_query('children'))
