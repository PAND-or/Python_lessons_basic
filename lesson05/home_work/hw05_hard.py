__author__ = "Андрей Петров"
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)

path = os.path.join(os.getcwd())

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")




def make_dir():
    if not arg:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), arg)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(arg))
    except FileExistsError:
        print('директория {} уже существует'.format(arg))

def del_dir():
    if not arg:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), arg)
    if (input('Удалить {} ? 0 - нет, 1 - да '.format(arg)) == int(1)):
        try:
            os.rmdir(dir_path)
            print('директория {} удалена'.format(arg))
        except FileExistsError:
            print('директории {} не существует'.format(arg))

def del_file():
    if not arg:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), arg)
    if (input('Удалить {} ? 0 - нет, 1 - да '.format(arg)) == int(1)):
        try:
            os.remove(dir_path)
            print('файл {} удален'.format(arg))
        except FileExistsError:
            print('файла {} не существует'.format(arg))
            
def path_dir():
    print(os.listdir(path))
    
def chenge_dir():
    if not arg:
        print("Необходимо указать имя директории вторым параметром")
        return
    path = os.path.join(arg)
    print(path)
    print(path_dir)

def copy_file():
    if not arg:
        print("Необходимо указать имя файла вторым параметром")
        return
    shutil.copy(arg, arg + r'.copy.py')
    
def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp':  copy_file,
    'rm': del_file,
    'cd': chenge_dir,
    'ls': path_dir
}

try:
    arg = sys.argv[2]
except IndexError:
    arg = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
