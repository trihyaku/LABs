city_codes = {
    495: ("Москва", 6),
    383: ("Новосибирск", 4),
    343: ("Екатеринбург", 5),
    381: ("Омск", 8),
    473: ("Воронеж", 3)
}

code = int(input("Введите код города: "))
duration = int(input("Введите длительность переговоров (в минутах): "))

if code in city_codes:
    city, rate = city_codes[code]
    cost = duration * rate
    print(f"Стоимость переговоров с {city}: {cost} руб.")
else:
    print("Код города не найден")