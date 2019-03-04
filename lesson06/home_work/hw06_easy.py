__author__ = "Андрей Петров"

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math

class Triangle: 
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def lenth(self, n, m):
        return math.sqrt((m[0] - n[0])**2 + (m[1] - n[1])**2)
    
    @property
    def area(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        ac = self.lenth(self.a, self.c)
        p = self.perimeter / 2
        return math.sqrt(p*(p - ac) * (p - ab) * (p - bc))
    
    @property
    def perimeter(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        ac = self.lenth(self.a, self.c)
        return ab + bc + ac
    
    @property
    def height(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        ac = self.lenth(self.a, self.c)
        p = self.perimeter / 2
        return (2 / ac) * math.sqrt(p*(p - ac) * (p - ab) * (p - bc))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def lenth(self, n, m):
        return math.sqrt((m[0] - n[0])**2 + (m[1] - n[1])**2)
    
    @property
    def area(self):
        ad = self.lenth(self.a, self.d)
        bc = self.lenth(self.b, self.c)
        return 0.5 * self.height * (ad + bc)
    
    @property
    def perimeter(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        cd = self.lenth(self.c, self.d)
        ad = self.lenth(self.a, self.d) 
        return ab + bc + cd + ad
    
    @property
    def height(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        cd = self.lenth(self.c, self.d)
        ad = self.lenth(self.a, self.d)
        return math.sqrt(abs(ab**2 - (((ad - bc)**2 + ab**2 + cd**2)/(2*(ad - bc)))**2))
    
    
if __name__ == "__main__":
    triangle1 = Triangle((0,0), (0, 10), (10, 0))
    print('Площадь треугольника', triangle1.area)
    print('Периметр треугольника', triangle1.perimeter)
    print('Высота треугольника', triangle1.height)


    trapeze1 = Trapeze((0,0), (0, 10), (10, 10), (20, 0))
    print('Площадь трапеции', trapeze1.area)
    print('Периметр трапеции', trapeze1.perimeter)
    print('Высота трапеции', trapeze1.height)