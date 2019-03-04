__author__ = "Андрей Петров"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    feb = 0
    i = 1
    list_feb = [1,1] #чтобы не перезаписывать сумму, а сделать обращение по индексам
    n = n-1 if n > 1 else 0 #индекс начинается с 0, а порядковый порядковый номер с 1
    m -= 1 #первые два элемента уже посчитаны и записаны в массив
    while m > i: #посчитать M раз
        feb = list_feb[i] + list_feb[i-1]
        list_feb.append(feb)
        i += 1
    return list_feb[n:] #вернуть лист фебоначи с элемента n
print(fibonacci(1,10))

#Сделать рекурсией

def fibRecurson(n,m):
    n = n if n > 0 else 1 #0 нельзя
    return list(map(lambda f: fib(f - 1) + fib(f - 2) if f > 2 else 1, range(n, m+1)))
print(fibRecurson(1,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1 
    while n < len(origin_list):
         for i in range(len(origin_list)-n):
              if origin_list[i] > origin_list[i+1]:
                   origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
         n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = [1, -4, 6, 8, -10]
def func(x):
    if x > 0:
        return 1
    else:
        return 0
    
def my_filter(funcion, listing):
    newlist = []
    for val in listing:
        if funcion(val):
            newlist.append(val)
    return newlist
    
print(list(filter(func, a)))
print(my_filter(func, a))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

my_points = ((0,1), (0,0), (1,0), (1,1))

print(my_points)

def check_squard(points):
    # Паралеллограм это четырех угольник у которого 2 стороны парралельны друг другу
    # построим 
    if(len(points) != 4):
        return False
    lines = []
    match = 0
    for i, point in enumerate(points):
        j = i+1
        while j < 4: #построение графов 
            another_point = points[j]
            try:
                k =  int((point[1] - another_point[1]) / (point[0] - another_point[0])) #угловые кооэфициенты прямых
            except ZeroDivisionError:
                k = 'inf'
            lines.append(k)
            if lines.count(k) == 2: #если есть 2 парралельные прямые
                match += 1
            j +=1
    return match == 2 #две парралельные прямые Бинго
check_squard(my_points)

