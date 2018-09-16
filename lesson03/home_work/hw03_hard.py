__author__ = "Андрей Петров"

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def arithmetic(a, b):
    c = [0,0]
    c[0] = (a[0]  * b[1]) + (b[0] * a[1]) #числитель
    c[1] = a[1]*b[1] #знаменатель
    return c 

def fractionConversion(a): #функция преобразования списка "n, x, y" в список "x" "y", с перестановкой минуса в числитель
    if(a[1] == 0 or a[2] == 0): #целое число в дробь
        return [a[0], 1]
    elif a[0] == 0: #возврат результата если нет целой части
        return [(a[1]*a[2]//abs(a[2])), abs(a[2])]
    else:
        res = [0,0]
        res[0] = abs(a[1]) + abs(a[0])*a[2] 
        res[0] = res[0]*a[0]//abs(a[0])*a[1]//abs(a[1])*a[2]//abs(a[2]) #перевод минуса в числитель, если он есть
        res[1] = a[2]
        return(res)


def simplification(a):
    res = [0,a[0],a[1]]

    if abs(a[0]) > abs(a[1]): #определение целой части
        num = int(a[0]/a[1])
        res[0] = num 
        res[1] = abs(a[0] - (a[1] * num))
        if(res[1] ==  0): #если вдруг в числителе появился 0, убрать и знаменатель
            res[2] = 0
    i = res[2]
    while i > 1: #сокращение дроби
        if((res[1] % i == 0) & (res[2] % i == 0)): #если и числитель и знаменатель делятся на одно число без остатка.
            res[1] = res[1] // i
            res[2] = res[2] // i
        i -= 1
    return res

def strToList(string):
    import re
    data_split = list(string.split(' '))
    
    sign = True
    lst = []
    
    digits, numerator, denominator,  = 0, 0, 0 #целое число, числитель, знаменатель
    
    for i in data_split:
        if(re.fullmatch('[-+]?\d+', i) is not None):
            if sign == False:
                digits =  0 - int(i)
                sign = True
            else:
                digits = int(i)
        elif(re.fullmatch('[-+]?\d+\/[-+]?\d+', i) is not None):
            if sign == False:
                numerator = 0 - int(i.split('/')[0])
                denominator = int(i.split('/')[1])
                sign = True
            else:
                numerator = int(i.split('/')[0])
                denominator = int(i.split('/')[1])
        elif(i == '-' or i == '+'):
            if (i == '-'):
                sign = False
            lst.append([digits, numerator, denominator])
            digits, numerator, denominator,  = 0, 0, 0 #обнуление для слудующей операции
    lst.append([digits, numerator, denominator]) #добавление последнего числв с список
    return lst

def resToString(lst):
    return '{} {}/{}'.format(lst[0],lst[1],lst[2])

def calculation(string):
    #print('input string', string)
    lst = strToList(string)
    #print('string to list',lst)
    
    res_sum = [0, 1]
    for i in lst:
        i = fractionConversion(i)
        res_sum = arithmetic(res_sum, i)
    #print('Арифметический результат', res_sum)
    res_simple = simplification(res_sum)
    #print('Упрощение дроби', res_simple)
    res_string = resToString(res_simple)
    return res_string

print('Пример ввода строк \n',
      '5/6 + 4/7\n',
      '-2/3 - -2\n',
      '2/3 + -2/4 + 4 3/2 + 6/3\n'
      
)
input_string = input('Введите строку для вычисления: ')
print(calculation(input_string))
#print('RESULT', calculation('5/6 + 4/7'), '\n')
#print('RESULT', calculation('-2/3 - -2'), '\n')
#print('RESULT', calculation('2/3 + -2/4 + 4 3/2 + 6/3'), '\n')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os
import re


dict_workers = {}

with open(os.path.join('data', 'workers'), 'r', encoding='UTF-8') as f_workers:
    for i, line in enumerate(f_workers):
        if i > 0:# пропуск первой строки
            result = re.split(r'\W+', line)
            dict_workers[str(result[0]+' '+result[1])] = {
                'salary': int(result[2]),
                'norm': int(result[4]),
                'pay_hours': float(int(result[2]) / int(result[4]))
            }
sumpayd = 0
with open(os.path.join('data', 'hours_of'), 'r', encoding='UTF-8') as f_hours_of:
    for i, line in enumerate(f_hours_of):
        if i > 0:# пропуск первой строки
            result = re.split(r'\W+', line)
            name = str(result[0]+' '+result[1])
            if dict_workers[name]['norm'] < int(result[2]):
                earned = dict_workers[name]['salary'] + (int(result[2]) - dict_workers[name]['norm']) * dict_workers[name]['pay_hours'] * 2
                #print(name, 'Переработал', 'норма', dict_workers[name]['norm'], 'отработал',  int(result[2]), 'зарплата', dict_workers[name]['salary'], 'Получит', earned)
            else:
                earned = int(result[2]) * dict_workers[name]['pay_hours']
                #print(name, 'Недоработал', 'норма', dict_workers[name]['norm'], 'отработал',  int(result[2]), 'Получит', earned)
            print('{:>15} - {:>5}руб.'.format(name, int(earned)))
            sumpayd += earned
print('Зарплата всех работников ', int(sumpayd))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
