import math

while True:
    print("\nВыберите тип фигуры:")
    print("K - Круг")
    print("T - Треугольник")
    print("П - Прямоугольник")
    figure = input("> ").lower()

    if figure == 'к':
        radius = float(input("Введите радиус круга: "))
        area = math.pi * radius ** 2
        print(f"Площадь круга: {area:.2f}")
    elif figure == 'т':
        a = float(input("Введите длину стороны A: "))
        b = float(input("Введите длину стороны B: "))
        c = float(input("Введите длину стороны C: "))
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Площадь треугольника: {area:.2f}")
    elif figure == 'п':
        a = float(input("Введите длину стороны A: "))
        b = float(input("Введите длину стороны B: "))
        area = a * b
        print(f"Площадь прямоугольника: {area:.2f}")
    else:
        print("Неизвестный тип фигуры")

    choice = input("Завершить работу? (Y/y): ")
    if choice.lower() == 'y':
        break