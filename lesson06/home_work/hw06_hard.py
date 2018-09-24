__author__ = "Андрей Петров"

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os
import re

class Workers():
    def __init__(self):
        self.list = []
        
    def addWorker(self, data):
        self.list.append(Worker(data))
    
    def getWorker(self, name):
        for i in self.list:
            if i.name == name:
                return i
        return None
        
    def earning(self, args):
        name = str(args[0] + ' ' + args[1])
        if not(self.getWorker(name) == None):
            self.getWorker(name).earn(int(args[2]))
            
    @property   
    def getSum(self):
        esum = 0
        for i in self.list:
            esum += i.earned
        return int(esum)
    
    @property    
    def showlist(self):
        return [i.name for i in self.list]
    
    @property    
    def showearnlist(self):
        return [(i.name, i.earned ) for i in self.list]

    
class Worker():
    def __init__(self, args):
        self.name = str(args[0] + ' ' + args[1])
        self.salary = int(args[2])
        self.norm = int(args[4])
        self.position = args[3]
        self.pay_hours = float(int(args[2])/int(args[4]))
                                                                 
    def earn(self, worked):
        if self.norm < worked:
            self.earned = self.salary + (worked - self.norm) * self.pay_hours * 2
            #print(self.name, 'Переработал', 'норма', self.norm, 'отработал',  worked, 'зарплата', self.salary, 'Получит', self.earned)
        else:
            self.earned = worked * self.pay_hours
            #print(self.name, 'Недоработал', 'норма', self.norm, 'отработал',  worked, 'Получит', self.earned)
        return self.earned

if __name__ == "__main__":
    
    workers = Workers()

    with open(os.path.join('data', 'workers'), 'r', encoding='UTF-8') as f_workers:
        for i, line in enumerate(f_workers):
            if i > 0:# пропуск первой строки
                result = re.split(r'\W+', line)
                workers.addWorker(result)      


    with open(os.path.join('data', 'hours_of'), 'r', encoding='UTF-8') as f_hours_of:
        for i, line in enumerate(f_hours_of):
            if i > 0:# пропуск первой строки
                result = re.split(r'\W+', line)
                workers.earning(result)
                
                
    print(workers.showearnlist)
    print('Зарплата всех работников ', workers.getSum)
