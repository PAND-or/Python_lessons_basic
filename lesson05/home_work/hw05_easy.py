__author__ = "Андрей Петров"

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import inspect

def create_dir():
    if not((os.path.exists('dir_1')) & (os.path.exists('dir_2'))):
        os.makedirs('dir_1')
        os.makedirs('dir_2')
def remove_dir():
    if ((os.path.exists('dir_1')) & (os.path.exists('dir_2'))):
        os.rmdir('dir_1')
        os.rmdir('dir_2')

create_dir()
remove_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_dir():
    path = os.path.curdir
    for root, dirs, files in  os.walk(path):
        print(root)
view_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

current = os.path.abspath(inspect.getsourcefile(lambda:0))
shutil.copy(current, r'copy_file.py')