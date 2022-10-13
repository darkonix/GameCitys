check_list = []


# Декоратор check_point, с его помощью регистрируем любые нужные нам методы, как методы проверки города от пользователя
def check_point(fun):
    check_list.append(fun)
    return fun


# Приводим название города в общий вид
def normalize_city_name(name):
    return name.strip().lower().replace('ё', 'е')


def is_city_startswith_char(city, char):
    return False


def is_non_cached(city, cache):
    return False


def get_next_char(city):
    return ""
