check_list = []


# Декоратор check_point, с его помощью регистрируем любые нужные нам методы, как методы проверки города от пользователя
def check_point(fun):
    check_list.append(fun)
    return fun


# Приводим название города в общий вид
def normalize_city_name(name):
    return name.strip().lower().replace('ё', 'е')


# Проверка, что город начинается с нужной буквы
def is_city_startswith_char(city, char):
    if char is None or city.startswith(char):
        return True
    else:
        print(f'Город должен начинаться с буквы {char.capitalize()}.')
    return False


def is_non_cached(city, cache):
    return False


def get_next_char(city):
    return ""
