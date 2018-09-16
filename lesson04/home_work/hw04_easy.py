__author__ = "Андрей Петров"

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst_first = [random.randint(-10, 10) for _ in range(10)]
print(lst_first)
lst_second = [i**2 for i in lst_first]
print(lst_second)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_first = ['apple', 'banana', 'qiwi']
fruits_second = ['apple', 'tomato', 'banana', 'potato']

fruits_result = [f for f in fruits_first if f in fruits_second]
print(fruits_result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst_rand = [random.randint(-100, 100) for _ in range(20)]
print(lst_first)
lst_third = [num for num in lst_rand if ((num % 4 != 0) & (num % 3 == 0) & (num > 0))]
print(lst_third)