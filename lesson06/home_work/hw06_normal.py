# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self):
        self.teachers = []
        self.classes = []

    def getClass(self, room_name):
        for i in self.classes:
            if i.name == room_name:
                return i
        return None

    @property
    def listClasses(self):
        return [i.name for i in self.classes]
    
    @staticmethod
    def getStudents(room_name):
        return school.getClass(room_name).listStudents
    
    @staticmethod
    def getTeachers(room_name):
        return school.getClass(room_name).listTeachers


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        school.classes.append(self)
    
    @property
    def listStudents(self):
        return [i.fullName for i in self.students]

    @property
    def listTeachers(self):
        return [i.fullName for i in self.teachers]

    
class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @property
    def fullName(self):
        return self.name + ' ' + self.surname

        
class Student(People):
    def __init__(self, name, surname, class_room, parents):
        People.__init__(self, name, surname)
        self.parents = self.addParrent(parents)
        self.class_room = self.addClass(class_room)
        self.class_room.students.append(self)
        
    def addClass(self, class_room):
        if school.getClass(class_room) == None:
            return ClassRoom(class_room)
        else: 
            return school.getClass(class_room) 

    @staticmethod
    def addParrent(parents):
        return [People(i[0], i[1]) for i in parents]
    
    @property
    def listSubjects(self):
        return [i.courses for i in self.class_room.teachers]
    
    @property
    def listParrents(self):
        return [i.fullName for i in self.parents]

    
class Teacher(People):
    def __init__(self, name, surname, teach_classes, courses):
        People.__init__(self, name, surname)
        self.teach_classes = []
        self.courses = courses
        self.teach_classes = teach_classes
        self.addClass(teach_classes)
        school.teachers.append(self)
        
    def addClass(self, teach_classes):
        for teach_class in teach_classes: 
            if school.getClass(teach_class) == None:
                ClassRoom(teach_class).teachers.append(self)
            else: 
                school.getClass(teach_class).teachers.append(self)

        
if __name__ == "__main__":
    school = School()
    
    students = [Student("Александр", "Иванов", "5 А", [("Андрей", "Иванов"), ("Алла", "Иванова")]),
                Student("Петр", "Сидоров", "8 Б", [("Петр", "Сидоров"), ("Ирина", "Сидорова")]),
                Student("Иван", "Петров", "4 В", [("Владимир", "Петров"), ("Татьяна", "Петрова")]),
                Student("Петр", "Федоров", "8 Б", [("Алексей", "Федоров"), ("Ольга", "Федорова")]),
                Student("Андрей", "Емельянов", "4 В", [("Семен", "Емельянов"), ("Елена", "Емельянова")]),
                Student("Владимир", "Курьянов", "8 Б", [("Павел", "Курьянов"), ("Алина", "Курьянова")]),
                Student("Константин", "Спиридонов", "4 В", [("Олег", "Спиридонов"), ("Карина", "Спиридонова")]),
                ]
    
    teachers = [Teacher("Александра", "Иванова", ["5 А", "8 Б", "4 В"], "Математика"),
                Teacher("Татьяна", "Семенова", ["5 А", "4 В"], "Биология"),
                Teacher("Иван", "Тетерев", ["4 В"], "Труд"),
                ]
    
    print('Список классов школы', school.listClasses)
    print('Список студентов 8Б', school.getStudents("8 Б"))
    print('Список предметов первого студента', students[0].listSubjects)
    print('Фио родителей первого студента', students[0].listParrents)
    print('Список учителей 5А класса', school.getTeachers("5 А"))