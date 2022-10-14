check_list = []


# Декоратор check_point, с его помощью регистрируем любые нужные нам методы, как методы проверки города от пользователя
def check_point(fun):
    check_list.append(fun)
    return fun


# Приводим название города в общий вид
def normalize_city_name(name):
    return name.strip().lower().replace('ё', 'е')


# Проверка, что город начинается с нужной буквы
@check_point
def is_city_startswith_char(city, char):
    if char is None or city.startswith(char):
        return True
    else:
        print(f'Город должен начинаться с буквы {char.capitalize()}.')
    return False


# Проверка, что город ещё не был назван
@check_point
def is_non_cached(city, cache, **kwargs):
    if city not in cache:
        return True
    else:
        print("Этот город уже был назван.")
        return False


# Проверка, что такой город существует и он известен нам
@check_point
def is_available(city, cities, **kwargs):
    if city in cities:
        return True
    else:
        print("Такого города не существует в России")
        return False


def get_next_char(city):
    return ""
