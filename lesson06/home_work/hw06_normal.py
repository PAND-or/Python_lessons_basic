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

class Scool:
    def __init__(self):
        self.teachers = []
        self.classes = []

    def getClasses(self):
        all_classes = [i.name for i in self.classes]
        return all_classes
    
    def getClass(self, room_name):
        for i in self.classes:
            if i.name == room_name:
                return i
        else:
            return None
    
    def getStudents(self, room_name):
        return scool.getClass(room_name).getStudents()
    
    def getTeachers(self, room_name):
        return scool.getClass(room_name).getTeachers()

    
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        scool.classes.append(self)
    
    def getStudents(self):
        all_students = [i.get_full_name() for i in self.students]
        return all_students

    def getTeachers(self):
        all_teachers = [i.get_full_name() for i in self.teachers]
        return all_teachers

    
class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname

        
class Student(People):
    def __init__(self, name, surname, class_room, parents):
        People.__init__(self, name, surname)
        self.parents = [People(i[0], i[1]) for i in parents]
        if scool.getClass(class_room) == None:
            self.class_room = ClassRoom(class_room)
        else: 
            self.class_room = scool.getClass(class_room) 
        self.class_room.students.append(self)

    def listSubjects(self):
        all_subjects = [i.courses for i in self.class_room.teachers]
        return all_subjects
    
    def getParrents(self):
        all_parents = [i.get_full_name() for i in self.parents]
        return all_parents

    
class Teacher(People):
    def __init__(self, name, surname, teach_classes, courses):
        People.__init__(self, name, surname)
        self.teach_classes = []
        for teach_class in teach_classes: #добавление этого учителя во все классы в которых он преподает
            if scool.getClass(teach_class) == None:
                ClassRoom(teach_class).teachers.append(self)
            else: 
                scool.getClass(teach_class).teachers.append(self)
        self.courses = courses
        self.teach_classes = teach_classes
        scool.teachers.append(self)

if __name__ == "__main__":
    scool = Scool()
    
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
    
    print('Список классов школы', scool.getClasses())
    print('Список студентов 8Б', scool.getStudents("8 Б"))
    print('Список предметов первого студента', students[0].listSubjects())
    print('Фио родителей первого студента', students[0].getParrents())
    print('Список учителей 5А класса', scool.getTeachers("5 А"))
