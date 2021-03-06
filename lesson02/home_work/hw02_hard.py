__author__ = 'Петров Андрей'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

pos_equal = equation.index("=")
pos_x = equation.index("x")
pos_plus = equation.index("+")

k = float(equation[pos_equal+1:pos_x])
b = float(equation[pos_plus+1:])

print('k = {}'.format(k))
print('b = {}'.format(b))
print('y = {}'.format(x * k + b))


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

print(
    "Пример корректной даты \n",
    "01.11.1985 \n\n",
    "Примеры некорректных дат\n",
    "01.22.1001\n",
    "1.12.1001\n",
    "-2.10.3001\n",
    "31.06.3001\n",
)


data_lenght = { #справочник длин диапазонов
    1:  31, 
    2:  29,  
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,  
    9: 30,  
    10: 31,  
    11: 30,  
    12: 31,  
    'year': 9999,  
    'month': 12  
}


date_input = input('Введите дату в формате dd.mm.yyyy: ')

def check_data(dinput):
    import re
    try:
        data_split = list(map(int, dinput.split('.')))
        match = re.fullmatch('\d{2}.\d{2}.\d{4}', dinput)

        if not(
            (data_split[0] <= data_lenght[data_split[1]]) &
            (data_split[1] <= data_lenght['month']) &
            (data_split[2] <= data_lenght['year']) & (match is not None)
        ):
            return False
        else:
            return True
    except:
        return False

while True:
    res = check_data(date_input)
    if(res):
        break
    else:
        print("Не верный формат!")
        date_input = input('Введите дату в формате dd.mm.yyyy: ')




# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = int(input('Номер комнаты: '))

#в условии задачи есть закономерность в кол-ве комнат 1, по 2 комнаты на двух этажах 2х2, по 3 комнаты на трех этажах 3х3.
claster = 1 #Кластер комнат, зная номер кластера можно сказать по сколько комнат на этом этаже
sum_rooms = 1 #Сумма всех комнат в кластерах

while n > sum_rooms: #Перебираем комнаты по кластерам, пока не найдем нужный кластер
    claster += 1
    sum_rooms += claster ** 2 #порядковый номер кластера в квадрете, к сумме прошдых комнат
    
max_floor = int((claster + 1) * claster / 2) #Максимальный номер этажа в кластере

dif_rooms = sum_rooms - n #Кол-во пропущенных комнат сверху кластера
floor = max_floor - (dif_rooms // claster) #от последнего этажа кластера вычитаем кол-во пропущенныъ этажей

max_room = claster #максимальное кол-во комнат на этаже равно номеру кластера
room = max_room - dif_rooms % max_room #порядковый номер комнаты, от максимального кол-ва комнат на этаже
print('Этаж {}, номер комнаты слева {}'.format(floor, room))