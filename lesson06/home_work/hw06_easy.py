# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math
class Triangle:
   
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        return 0.5 * abs((self.a[0]- self.c[0]) * (self.b[1] - self.c[1]) - (self.b[0] - self.c[0])*(self.a[1] - self.c[1]))
    def perimeter(self):
        return math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2) +  math.sqrt((self.c[0] - self.b[0])**2 + (self.c[1] - self.b[1])**2) +  math.sqrt((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)
    def height(self):
        return 2 * self.area() / math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2)

triangle1 = Triangle((0,0), (0, 10), (10, 0))
print(triangle1.b)
print(triangle1.area())
print(triangle1.perimeter())
print(triangle1.height())

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
    def area(self):
        ad = self.lenth(self.a, self.d)
        bc = self.lenth(self.b, self.c)
        return 0.5 * self.height() * (ad + bc)
    def perimeter(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        cd = self.lenth(self.c, self.d)
        ad = self.lenth(self.a, self.d) 
        return ab + bc + cd + ad
    def height(self):
        ab = self.lenth(self.a, self.b)
        bc = self.lenth(self.b, self.c)
        cd = self.lenth(self.c, self.d)
        ad = self.lenth(self.a, self.d)
        return math.sqrt(abs(ab**2 - (((ad - bc)**2 + ab**2 + cd**2)/(2*(ad - bc)))**2))

trapeze1 = Trapeze((0,0), (0, 10), (10, 10), (20, 0))
print(trapeze1.b)
print(trapeze1.area())
print(trapeze1.perimeter())
print(trapeze1.height())