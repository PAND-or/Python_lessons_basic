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


days_of_mounth = { #справочник кол-ва дней в месяце
    1: {
        'days': 31, 
        'name': 'январе'
    },
    2:  {
        'days': 29,  
        'name': 'феврале'
    },
    3:  {
        'days': 31,  
        'name': 'марте'
    },
    4:  {
        'days': 30,  
        'name': 'апреле'
    },
    5:  {
        'days': 31,  
        'name': 'мае'
    },
    6:  {
        'days': 30,  
        'name': 'июне'
    },
    7:  {
        'days': 31,  
        'name': 'июле'
    },
    8:  {
        'days': 31,  
        'name': 'августе'
    },
    9:  {
        'days': 30,  
        'name': 'сентябре'
    },
    10:  {
        'days': 31,  
        'name': 'октябре'
    },
    11:  {
        'days': 30,  
        'name': 'ноябре'
    },
    12:  {
        'days': 31,  
        'name': 'декабре'
    },
}


date_input = input('Введите дату в формате dd.mm.yyyy: ')


def check_data(dinput):
    data = dinput.split('.')

    if len(data) != 3:
        res_message = 'Формат даты указан не верно, либо разделитель не точка'
        res_check = False
    elif(not( #проверка на длинну строки
            (len(data[0]) == 2) & 
            (len(data[1]) == 2) & 
            (len(data[2]) == 4)
        )
    ): 
        res_message = 'Не верная длина вводимых символов'
        res_check = False
    elif not( #проверка, можно ли приобразовать к int
        (data[0].isdigit()) & 
        (data[1].isdigit()) & 
        (data[2].isdigit())
    ):
        res_message = 'Формат даты указан не верно, символ не число'
        res_check = False
    elif not( # попадают ли в допустимые диапазоны
        (int(data[0]) <= 31) & 
        (int(data[0]) >= 1) & 
        (int(data[1]) <= 12) & 
        (int(data[1]) >= 1) & 
        (int(data[2]) <= 9999) & 
        (int(data[2]) >= 1)
    ):
        res_message = 'Не соответствует допустимому диапазону'
        res_check = False
    elif not( #проверка на 31, 30, 28 дней месяца (без учета високосного года)
        int(data[0]) <= days_of_mounth[int(data[1])]['days']
    ):
        res_message = 'В {} {} дней, введено {}'.format(days_of_mounth[int(data[1])]['name'], days_of_mounth[int(data[1])]['days'], data[0])
        res_check = False
    else:
        res_message = 'Все норм, дата в правильном формате'
        res_check = True
    return [res_check, res_message]


while True:
    res = check_data(date_input)
    if(res[0]):
        print(res[1])
        break
    else:
        print(res[1])
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