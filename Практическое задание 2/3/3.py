sale_amount = float(input("Введите сумму продажи: "))

if sale_amount < 5000:
    discount = 5
elif sale_amount < 15000:
    discount = 12
elif sale_amount < 25000:
    discount = 20
else:
    discount = 30

discount_amount = sale_amount * discount / 100
final_amount = sale_amount - discount_amount

print(f"Скидка: {discount}% ({discount_amount:.1f} руб.)")
print(f"Итоговая сумма: {final_amount:.1f} руб.")