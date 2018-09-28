__author__ = "Андрей Петров"

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
        self.students = []

    def get_class(self, room_name):
        for i in self.classes:
            if i.name == room_name:
                return i
        return None
    
    def get_students_by_fullname(self, fullname):
        for i in self.students:
            if i.full_name == fullname:
                return i
        return None

    def get_students_by_room(self, room_name):
        classroom = self.get_class(room_name)
        if not classroom == None:
            return classroom.list_students
        else:
            return None
        
    def add_student(self, name, surname, class_room, parents):
        student = Student(name, surname, class_room, parents)
        classroom = self.add_class(class_room)
        student.class_room = classroom
        self.students.append(student)
        classroom.students.append(student)        
        return student
    
    def add_teacher(self, name, surname, teach_classes, courses):
        teacher = Teacher(name, surname, teach_classes, courses)
        self.teachers.append(teacher)
        for teach_class in teach_classes:
            classroom = self.add_class(teach_class)
            classroom.teachers.append(teacher)
        return teacher
                
    def add_class(self, class_room):
        if self.get_class(class_room) == None:
            class_obj = ClassRoom(class_room)
            self.classes.append(class_obj)
            return class_obj
        else: 
            return self.get_class(class_room)
        
    @property
    def list_classes(self):
        return [i.name for i in self.classes]

    def get_teachers(self, room_name):
        classroom = self.get_class(room_name)
        if not classroom == None:
            return classroom.list_teachers
        else:
            return None


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
    
    @property
    def list_students(self):
        return [i.full_name for i in self.students]

    @property
    def list_teachers(self):
        return [i.full_name for i in self.teachers]

    
class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @property
    def full_name(self):
        return self.name + ' ' + self.surname

        
class Student(People):
    def __init__(self, name, surname, class_room, parents):
        People.__init__(self, name, surname)
        self.parents = self.add_parrent(parents)
        self.class_room = class_room

    @staticmethod
    def add_parrent(parents):
        return [People(i[0], i[1]) for i in parents]
    
    @property
    def list_subjects(self):
        
        return [i.courses for i in self.class_room.teachers]
    
    @property
    def list_parrents(self):
        return [i.full_name for i in self.parents]

    
class Teacher(People):
    def __init__(self, name, surname, teach_classes, courses):
        People.__init__(self, name, surname)
        self.teach_classes = []
        self.courses = courses
        self.teach_classes = teach_classes

        
if __name__ == "__main__":
    schooll = School()

    schooll.add_student("Александр", "Иванов", "5 А", [("Андрей", "Иванов"), ("Алла", "Иванова")])
    schooll.add_student("Петр", "Сидоров", "8 Б", [("Петр", "Сидоров"), ("Ирина", "Сидорова")])
    schooll.add_student("Иван", "Петров", "4 В", [("Владимир", "Петров"), ("Татьяна", "Петрова")])
    schooll.add_student("Петр", "Федоров", "8 Б", [("Алексей", "Федоров"), ("Ольга", "Федорова")])
    schooll.add_student("Андрей", "Емельянов", "4 В", [("Семен", "Емельянов"), ("Елена", "Емельянова")])
    schooll.add_student("Владимир", "Курьянов", "8 Б", [("Павел", "Курьянов"), ("Алина", "Курьянова")])
    schooll.add_student("Константин", "Спиридонов", "4 В", [("Олег", "Спиридонов"), ("Карина", "Спиридонова")])

    
    schooll.add_teacher("Александра", "Иванова", ["5 А", "8 Б", "4 В"], "Математика")
    schooll.add_teacher("Татьяна", "Семенова", ["5 А", "4 В"], "Биология")
    schooll.add_teacher("Иван", "Тетерев", ["4 В"], "Труд")
    
    print('Список классов школы', schooll.list_classes)
    print('Список студентов 8Б', schooll.get_students_by_room('8 Б'))
    print('Список предметов первого студента', schooll.get_students_by_fullname('Александр Иванов').list_subjects)
    print('Фио родителей первого студента', schooll.get_students_by_fullname('Александр Иванов').list_parrents)
    print('Список учителей 5А класса', schooll.get_teachers("5 А"))