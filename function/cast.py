import sqlite3


def get_all_actor(first_actor, second_actor):
    """
    Функция, которая получает в качестве аргумента имена двух актеров,
    сохраняет всех актеров из колонки cast.
    :param first_actor: первый актер.
    :param second_actor: второй актер.
    :return: возвращает всех актеров игравших с двумя актерами указанных в параметре.
    """
    with sqlite3.connect('../netflix.db') as connection:
        cursor = connection.cursor()
        # Фильтрация по результатам агрегации и группировки.
        query = f"""
            SELECT `cast`
            FROM netflix
            WHERE `cast` LIKE '%{first_actor}%' 
            AND `cast` LIKE '%{second_actor}%'
        """
        cursor.execute(query)
        result = []
        set_result = {}
        for actor in cursor.fetchall():
            result.extend(actor[0].split(', '))
            set_result = set(result)
            set_result.discard(first_actor)
            set_result.discard(second_actor)
        return list(set_result), result


def get_play_more_twice(data_actors):
    """
    Функция возвращает список тех, кто играет с актерами, указанными в функции
    get_all_actor(first_actor, second_actor), в паре больше 2 раз.
    :param data_actors: все актеры которые играют с актерами из парамера функции
    get_all_actor(first_actor, second_actor)
    :return: возвращает список тех, кто играет с актерами в паре больше 2 раз.
    """
    result = []
    for actor in data_actors[0]:
        if data_actors[1].count(actor) > 2:
            result.append(actor)
    return result


cast_ = get_all_actor("Rose McIver", "Ben Lamb")
result_ = get_play_more_twice(cast_)
print(result_)
