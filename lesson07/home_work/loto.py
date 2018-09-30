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
        self.barrels = Numbers(start, end)
        self.gamers = []
        
    def start(self):
        status = True
        while status:
            number = self.barrels.get_numbers
            print('Число на боченке {}'.format(number))
            
            for gamer in self.gamers:
                if len(gamer.card.list) == 0:
                    print('Game OVER Победил игрок {}'.format(gamer.name))
                    status = False
                    break
                if not gamer.do(number):
                    print('Из игры вылетает игрок {}'.format(gamer.name))
                    self.kick_gamer(gamer)
                    status = False
                    break
                    
    def kick_gamer(self, gamer):
        if gamer in self.gamers:
            self.gamers.remove(gamer)    

class GameBuilder:
    def __init__(self):
        self._game = None
        self.start = None
        self.end = None
        self.num = None
        
    def build(self):
        return self._game
    
    def set_start_num(self, num):
        self.start = num
        return self
   
    def set_end_num(self, num):
        self.end = num
        return self
    
    def set_num_num(self, num):
        self.num = num
        return self
    
    def build_game(self):
        self._game = Game(self.start, self.end)
        return self
        
    def add_player(self, desc):
        gamer = GamerFactory.get_gamer(desc, self.start, self.end, self.num)
        self._game.gamers.append(gamer)
        return self            

class GamerFactory:
    @staticmethod
    def get_gamer(name, *args):
        if name == "human":
            return UserGamer(name, *args)
        elif name == "computer":
            return AiGamer(name, *args)

        
class Gamer():
    def __init__(self, name, start, end, num_numbers):
        self.card = Cards(start, end, num_numbers)
        self.name = name

        
class AiGamer(Gamer):
    def __init__(self, name, start, end, num_numbers):
        super().__init__(name, start, end, num_numbers)

    def do(self, number):
        print('Карточка игрока: {}'.format(self.name))
        self.card.delete_numbers(number)
        print(self.card.print_str_card())
        return True


class UserGamer(Gamer):
    def __init__(self, name, start, end, num_numbers):
        super().__init__(name, start, end, num_numbers)
    
    def do(self, number):
        print('Карточка игрока: {}'.format(self.name))
        print(self.card.print_str_card())
        inp = input('Зачеркнуть или продолжить?: Y / N: ')
        if inp == "Y":
            if self.card.delete_numbers(number):
                print('Такой номер есть в карточке!')
                return True
            else:
                print('Game OVER Такой номер есть в карточке!')
                return False
        else:
            if self.card.delete_numbers(number):
                print('Game OVER Такой номер есть в карточке!')
                return False
            else:
                return True
                print('Верно! Такого номера нет в карточке!')


                
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

    def __init__(self, start, end, num_numbers):
        self.free_numbers = Numbers(start, end)
        self.list = random.sample(self.free_numbers.list, num_numbers)
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

    def mark_numbers(self, number):
        for line in self.lines:
            if number in line:
                index = line.index(number)
                line[index] = '-'

    def delete_numbers(self, number):
        if number in self.list:
            self.list.remove(number)
            self.mark_numbers(number)
            return True
        else:
            return False  
                
    def str_lines(self, line):
        return "".join("{:>4}".format(n) for n in line)
    
    def print_str_card(self):
        str_lines = []
        for line in self.lines:
            str_lines.append(self.str_lines(line))
        strcard = str('--------------------------\n{}\n{}\n{}\n--------------------------\n').format(str_lines[0], str_lines[1], str_lines[2])
        return strcard

    
if __name__ == "__main__":
    GameBuilder()\
        .set_start_num(1)\
        .set_end_num(91)\
        .set_num_num(15)\
        .build_game()\
        .add_player("human")\
        .add_player("computer")\
        .build()\
        .start()
