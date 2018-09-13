# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def input_data(name, date, city):
    print('{}, {} год(а), проживает в городе {}'.format(name.title(), date, city.title()))


input_data('василий', 21, 'москва')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_num(*args):
    max_arg = args[0]
    for i in args:
        if i > max_arg:
            max_arg = i
    return max_arg


print(max_num(3))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_len(*args):
    max_arg = args[0]
    for i in args:
        if len(i) > len(max_arg):
            max_arg = i
    return max_arg


print(max_len('fd', 'dsaf', 'zzzz'))
