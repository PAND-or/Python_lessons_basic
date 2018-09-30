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


class Game:
    def __init__(self, start, end):
        self.computer_card = Cards(start, end)
        self.user_card = Cards(start, end)
        self.barrels = Numbers(start, end)
        
    def start(self):
        print('Карточка компьютера \n', self.computer_card.print_str_card())
        print('\n Карточка Игрока \n', self.user_card.print_str_card())

        while True:
            if len(self.user_card.list) == 0:
                print('Game OVER Победил игрок')
            elif len(self.computer_card.list) == 0:
                print('Game OVER Победил компьютер')

            number = self.barrels.get_numbers
            print('Число на боченке {}'.format(number))

            inp = input('Зачеркнуть или продолжить?: Y / N: ')
            if inp == "Y":
                if self.user_card.delete_numbers(number):
                    print('Такой номер есть в карточке!')
                    self.computer_card.delete_numbers(number)
                else:
                    print('Game OVER Такой номер есть в карточке!')
                    break
            else:
                if self.user_card.delete_numbers(number):
                    print('Game OVER Такой номер есть в карточке!')
                    break
                else:
                    print('Верно! Такого номера нет в карточке!')
                    self.computer_card.delete_numbers(number)


class Numbers():
    def __init__(self, start, end):
        self.list = [i for i in range(start, end)]
 
    @property
    def get_numbers(self):
        number = random.choice(self.list)
        self.delete_numbers(number)
        return number
    
    def delete_numbers(self, number):
        if number in self.list:
            self.list.remove(number)
            return True
        else:
            return False
            
        

        
class Cards(Numbers):
    def __init__(self, start, end):
        self.numbers = Numbers(start, end)
        self.list = random.sample(self.numbers.list, 15)
        self.lines = self.create_lines()
        
    def create_lines(self):
        lines = [
            self.list[:5],
            self.list[5:10],
            self.list[10:15]
        ]
        for line in lines:
            line.sort()
        return lines
    
    def str_lines(self, line):
        str_line = ''
        for i, number in enumerate(line):
            if (i == 0) & (number < 10):
                str_line += str(number)
            elif(i == 0) & (number > 10):  
                str_line += '   ' + str(number)
            elif len(str_line) > 25:
                str_line += ' ' + str(number)
            elif (line[i] - line[i-1]) > 10:
                str_line += '   ' + str(number)
            else:
                str_line += ' ' + str(number)
        return str_line
    
    def print_str_card(self):
        str_lines = []
        for line in self.lines:
            str_lines.append(self.str_lines(line))
        strcard = str('--------------------------\n{}\n{}\n{}\n--------------------------\n').format(str_lines[0], str_lines[1], str_lines[2])
        return strcard

    
if __name__ == "__main__":
    
    game = Game(1, 91)
    game.start()
    
    
