# Все задачи текущего блока решите с помощью генераторов списков!

import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [random.randrange(0, 100) for _ in range(10)]
list2 = [i ** 2 for i in list1]
print(list1, list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_fruit = ['Мандарин', 'Апельсин', 'Яблоко', 'Банан']
list_fruit2 = ['Киви', 'Банан', 'Помелло', 'Ананас']
print(list(set(list_fruit) & set(list_fruit2)))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_result = [i for i in list1 if i % 3 == 0 and i > 0 and i % 4 != 0]
print(list_result)
