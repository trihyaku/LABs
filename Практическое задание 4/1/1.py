class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, длина = {self.length}"

rect1 = Rectangle(2, 8)
rect2 = Rectangle(4, 6)

for i, rect in enumerate([rect1, rect2], 1):
    print(f"\nПрямоугольник {i}:")
    print(rect)
    print(f"Площадь: {rect.area()}")
    print(f"Периметр: {rect.perimeter()}")