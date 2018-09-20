# Вам дан текст:

# Эти задачи необходимо решить используя регулярные выражения!

import re

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь
#  заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее
#  подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
# te_4_st@test.com - верно указан.

RE_NAME = '^[A-ZА-Я][a-zA-Zа-яА-Я]+$'
RE_EMAIL = '^[a-z0-9\_]+@[a-z0-9]+\.(ru|org|com)$'

name = input('Введите своё имя: ')
last_name = input('Введите свою фамилию: ')
email = input('Введите свой email: ')

if re.search(RE_NAME, name) and re.search(RE_NAME, last_name) and re.search(RE_EMAIL, email):
    print('Данные введены верно!')
else:
    if not re.search(RE_NAME, name):
        print('Имя введено не верно!')
    elif not re.search(RE_NAME, last_name):
        print('Фамилия  введена не верно!')
    elif not re.search(RE_EMAIL, email):
        print('Email введён не верно!')

# Задача - 2:
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
RE_DOTS = '[\.]{2}'

for line in some_str:
    if re.search(RE_DOTS, line):
        print(re.findall(RE_DOTS, line))

'''не справился с последним'''
