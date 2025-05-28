while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Сумма: {a + b}")

    choice = input("Завершить работу? (Y/y): ")
    if choice.lower() == 'y':
        break