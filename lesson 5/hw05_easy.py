import sys
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def creates_dir():
    try:
        i = 0
        while i < 9:
            i += 1
            os.mkdir('dir_{}'.format(i))
    except Exception as e:
        print(e)
    finally:
        print('Функция отработала!')


def del_dir():
    i = 0
    while i < 9:
        i += 1
        os.rmdir('dir_{}'.format(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_dir():
    try:
        l_dir = os.listdir()
        for l in l_dir:
            if os.path.isdir(l):
                print(l)
    except Exception as e:
        print(e)
    finally:
        print('Функция отработала!')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def cp_this_file():
    try:
        name_file = sys.argv[0]
        f_name_file, s_name_file = name_file.split('.')
        shutil.copyfile(name_file, '{}_cp.{}'.format(f_name_file, s_name_file))
    except Exception as e:
        print(e)
    finally:
        print('Функция отработала!')


if __name__ == '__main__':
    print('Что сделать?\n'
          '1.Создать директории\n'
          '2.Удалить директории\n'
          '3.Показать папки в текущей директории\n'
          '4.Скопировать текущий файл\n')
    try:
        num = int(input('Ваш выбор: '))
        if num == 1:
            creates_dir()
        elif num == 2:
            del_dir()
        elif num == 3:
            view_dir()
        elif num == 4:
            cp_this_file()
    except Exception as e:
        print(e)
    finally:
        print('Программа завершила работу!')
