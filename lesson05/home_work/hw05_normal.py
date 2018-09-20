__author__ = "Андрей Петров"

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os


def create_dir(new_dir):
    if not(os.path.exists(new_dir)):
        os.makedirs(new_dir)
        return True
    else:
        return False
def remove_dir(del_dir):
    if os.path.exists(del_dir):
        os.rmdir(del_dir)
        return True
    else:
        return False

def view_dir(path):
    return os.listdir(path)

print(
    'Выберете действие \n',
    '1 Перейти в папку\n',
    '2 Посмотреть содержимое текущей папки\n',
    '3 Удалить папку\n',
    '4 Создать папку\n',
    'q Для выхода',
    
)
path = ''
while True:
    print('Текущая папка', path)
    key = input('Введите команду: ')

    if len(path) == 0:
        path = os.path.curdir
        #path = os.path.abspath
    if key == '1':
        new_path = input('Введите путь: ')
        if os.path.exists(new_path):
            path = new_path
        else:
            print('Директория {} не найдена'.format(path))
    elif key == '2':
        dirs = view_dir(path)
        if len(dirs) > 0:
            print('Сожержимое текущей папки', dirs)
        else:
            print('Папка пустая')
    elif key == '3':
        del_path = input('Введите имя папки для удаления: ')
        if remove_dir(del_path):
            print('Директория {} удалена'.format(del_path))
        else:
            print('Директория {} не найдена'.format(del_path))
    elif key == '4':
        new_path = input('Введите имя папки для создания: ')
        if create_dir(new_path):
            print('Директория {} создана'.format(new_path))
        else:
            print('Директория {} уже есть'.format(new_path))
    elif key == 'q':
        sys.exit() 