year = int(input("Введите год: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} год - ВИСОКОСНЫЙ")
else:
    print(f"{year} год - НЕ ВИСОКОСНЫЙ")