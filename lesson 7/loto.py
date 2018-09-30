#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:

    def __init__(self, name):
        self.card = [
            ['-' for _ in range(9)],
            ['-' for _ in range(9)],
            ['-' for _ in range(9)]
        ]
        self.name = name
        self.line_1, self.line_2, self.line_3 = self.random_5()
        self.create_card()
        self.close_num = 0

    def create_card(self):
        for k in self.line_1:
            if k in self.line_2 and k in self.line_3:
                self.card[0][k] = random.randint(1, 8)
            elif k in self.line_2 or k in self.line_3:
                self.card[0][k] = random.randint(1, 9)
            else:
                self.card[0][k] = random.randint(1, 10)
        for k in self.line_2:
            if self.card[0][k] == '-' and k not in self.line_3:
                self.card[1][k] = random.randint(1, 10)
            elif self.card[0][k] == '-' and k in self.line_3:
                self.card[1][k] = random.randint(1, 9)
            elif self.card[0][k] != '-' and k in self.line_3:
                self.card[1][k] = random.randint(self.card[0][k] + 1, 9)
            else:
                self.card[1][k] = random.randint(self.card[0][k] + 1, 10)
        for k in self.line_3:
            if self.card[0][k] == '-' and self.card[1][k] == '-':
                self.card[2][k] = random.randint(1, 10)
            elif self.card[0][k] != '-' and self.card[1][k] == '-':
                self.card[2][k] = random.randint(self.card[0][k] + 1, 10)
            elif self.card[0][k] == '-' and self.card[1][k] != '-':
                self.card[2][k] = random.randint(self.card[1][k] + 1, 10)
            else:
                self.card[2][k] = random.randint(self.card[1][k] + 1, 10)

    @staticmethod
    def random_5():
        five_num_1 = [i for i in range(9)]
        five_num_2 = [i for i in range(9)]
        five_num_3 = [i for i in range(9)]
        for i in range(4):
            five_num_1.pop(random.randint(0, len(five_num_1) - 1))
        for i in range(4):
            five_num_2.pop(random.randint(0, len(five_num_2) - 1))
        for i in range(4):
            five_num_3.pop(random.randint(0, len(five_num_3) - 1))

        return five_num_1, five_num_2, five_num_3

    def output_card(self):
        print(('{}'.format(self.name)).center(36, '-'))
        for line in self.card:
            index = 0
            for num in line:
                if num == '-' or num == 'x':
                    print(str(num).rjust(3), end=' ')
                elif num == 10:
                    print(str(num * (index + 1)).rjust(3), end=' ')
                else:
                    print(str(num + index * 10).rjust(3), end=' ')
                index += 1
            print()
        print(''.center(36, '-'))

    def del_num(self, num):
        i = 0
        index = int(num / 100 * 10)
        for line in self.card:
            if num - index * 10 == 0 and line[index-1] == 10:
                self.card[i][index] = 'x'
                return True
            if line[index] == num - index * 10:
                self.card[i][index] = 'x'
                return True
            i += 1
        return False


class Game:

    def __init__(self):
        self.player = Card('Игрок')
        self.computer = Card('Компьютер')
        self.all_num = [i for i in range(1, 90)]

    def start(self):
        while self.player.close_num != 15 or self.computer.close_num != 15:
            self.computer.output_card()
            self.player.output_card()
            rand = self.all_num[random.randint(1, len(self.all_num) - 1)]
            print('\nВыпадает бочонок с номером: {}\n'.format(rand))
            answer = input('Удалить данную цифру с карточки? (д/н) ')
            search_num_player = self.player.del_num(rand)
            search_num_computer = self.computer.del_num(rand)
            if search_num_player and (answer == 'д' or answer == 'да'):
                print('Цифра закрыта! \n')
            elif not search_num_player and (answer == 'н' or answer == 'нет'):
                print('Продолжаем!')
            else:
                print('Вы ошиблись, проигрыш!')
                print('Game over!')
                return 0
            self.all_num.pop(rand - 1)
        print('Вы победили! Поздравляем!')

game = Game()
game.start()

