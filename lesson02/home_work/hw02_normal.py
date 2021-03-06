__author__ = 'Петров Андрей'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


test_list = [2, -5, 8, 9, -25, 25, 4] 
print('Тестовые данные', test_list)

def isqrt(n): #метод Ньютона
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

new_list = []

for i in test_list:
    if(i == isqrt(i)**2):
        new_list.append(isqrt(i))
print('Результат', new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date_input = '02.11.2013'

months = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
days = ['первое','второе','третье','четвертое','пятое','шестое','седьмое','восьмое','девятое','десятое','одинадцатое','двенадцатое','тринадцатое','четырнадцатое','пятнадцатое','шестнадцатое','семнадцатое','восемнадцатое','девятнадцатое','двадцатое','двадцать первое','двадцать второе','двадцать третье','двадцать четвертое','двадцать пятое','двадцать шестое','двадцать седьмое','двадцать восьмое','двадцать девятое','тридцатое','тридцать первое']

data = date_input.split('.')
days[int(data[0]) -1], months[int(data[1]) -1], data[2]


print('{} {} {} года. '.format(days[int(data[0]) -1], months[int(data[1]) -1], data[2]))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n = input('Количество элементов списка: ')

from random import randint
i=0
list = []
while i < int(n): #генерация случайного списка из целых чисел
    list.append(randint(-100, 100))
    i += 1
print(list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
print(lst)

lst2 = list(set(lst))
print(lst2)

lst3 = []
for i in lst:
    if lst.count(i) == 1:
        lst3.append(i)
print(lst3)