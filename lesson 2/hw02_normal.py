import random
import math

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
random_list = []
rez_random_list = []
size_random_list = random.randrange(3, 20)
x = 0
while x < size_random_list:
    random_list.append(random.randrange(0, 100, 1, _int=int))
    x += 1
print(random_list)

for z in random_list:
    if math.sqrt(z) == int(math.sqrt(z)):
        rez_random_list.append(int(math.sqrt(z)))
print(rez_random_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

list_date_text_day = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвёртое', 5: 'пятое', 6: 'шестое',
                      7: 'седьмое', 8: 'возьмое', 9: 'девятое', 10: 'десятое', 11: 'одиннадцатое',
                      12: 'двенадцатое', 13: 'тринадцатое', 14: 'четырнадцатое', 15: 'пятнадцатое',
                      16: 'шестнадцатое', 17: 'семнадцатое', 18: 'восемнадцатое', 19: 'девятнадцатое',
                      20: 'двадцатое', 21: 'двадцать', 30: 'тридцатое', 31: 'тридцать'}
list_date_text_month = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
                        9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
date_input = input('Enter date(example: 2.11.2008): ')
date_input = date_input.split('.')

# if date_input[0][0] == '0':
#     day = list_date_text_day.get(date_input[0][1])
# else:
#     if date_input[0][1] == '0':
#         day = list_date_text_day.get(date_input[0][0]*10)
#     else:
#         day = str(list_date_text_day.get(int((date_input[0])[0]) * 10))
#         day = day + str(list_date_text_day.get(int((date_input[0])[1])))
day = int(date_input[0])
month = int(date_input[1])
# create day text
if day < 21 or day == 30:
    day = str(list_date_text_day.get(day))
else:
    day = str(list_date_text_day.get(day // 10 * 10 + 1)) + ' ' + str(list_date_text_day.get(day % 10))
# create month text
if 0 < month < 13:
    month = str(list_date_text_month.get(month))
else:
    print('Error type date!!!')
print(day, month, date_input[2], 'года')
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

random_list = []
size_random_list = int(input('Сколько чисел принять в список: '))
x = 0
while x < size_random_list:
    random_list.append(random.randrange(-100, 100, 1, _int=int))
    x += 1
print(random_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
