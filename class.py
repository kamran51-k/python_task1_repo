import math
class Circle:

    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return f'Circle Area: {math.pi * self.radius ** 2}'
    def perimeter(self):
        return f'Circle perimeter: {2 * math.pi * self.radius}'
circle = Circle(5)
print(circle.area())
print(circle.perimeter())
class Duzbucaqli:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return f'duzbucaqli Area: {self.a * self.b}'
    def perimeter(self):
        return f'duzbucaqli perimeter:{self.a * 2 + self.b * 2}'    
a = Duzbucaqli(10,20)
# print(a.area())
# print(a.perimeter())







