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

class Numbers():
    def __init__(self):
        self.list = [i for i in range(1, 91)]
 
    @property
    def getNumbers(self):
        number = random.choice(self.list)
        self.deleteNumbers(number)
        return number
    
    def deleteNumbers(self, number):
        if number in self.list:
            self.list.remove(number)
            return True
        else:
            return False
            
        

        
class Cards(Numbers):
    def __init__(self):
        self.numbers = Numbers()
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
        strLine = ''
        for i, number in enumerate(line):
            if (i == 0) & (number < 10):
                strLine += str(number)
            elif(i == 0) & (number > 10):  
                strLine += '   ' + str(number)
            elif len(strLine) > 25:
                strLine += ' ' + str(number)
            elif (line[i] - line[i-1]) > 10:
                strLine += '   ' + str(number)
            else:
                strLine += ' ' + str(number)
        return strLine
    
    def printStrCard(self):
        strLines = []
        for line in self.lines:
            strLines.append(self.str_lines(line))
        strcard = str('--------------------------\n{}\n{}\n{}\n--------------------------\n').format(strLines[0], strLines[1], strLines[2])
        return strcard


if __name__ == "__main__":

    computer_card = Cards()
    user_card = Cards()
    barrels = Numbers()

    print('Карточка компьютера \n', computer_card.printStrCard())
    print('\n Карточка Игрока \n', user_card.printStrCard())

    while True:
        if len(user_card.list) == 0:
            print('Game OVER Победил игрок')
        elif len(computer_card.list) == 0:
            print('Game OVER Победил компьютер')

        number = barrels.getNumbers
        print('Число на боченке {}'.format(number))

        inp = input('Зачеркнуть или продолжить?: Y / N: ')
        if inp == "Y":
            if user_card.deleteNumbers(number):
                print('Такой номер есть в карточке!')
                computer_card.deleteNumbers(number)
            else:
                print('Game OVER Такой номер есть в карточке!')
                break
        else:
            if user_card.deleteNumbers(number):
                print('Game OVER Такой номер есть в карточке!')
                break
            else:
                print('Верно! Такого номера нет в карточке!')
                computer_card.deleteNumbers(number)
        
