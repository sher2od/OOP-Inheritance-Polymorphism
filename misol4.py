import math

# Bosh sinf (parent class)
class Shape:
    def area(self):
        raise NotImplementedError("area() metodi har bir shakl uchun alohida yozilishi kerak")

# Aylana klassi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# To'g'ri to'rtburchak klassi
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Uchburchak klassi
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} yuzasi: {shape.area():.2f}")
