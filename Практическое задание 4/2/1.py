class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}. Новый баланс: {self.balance}")
        else:
            print("Ошибка: Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Ошибка: Недостаточно средств. Запрошено: {amount}, доступно: {self.balance}")
        elif amount <= 0:
            print("Ошибка: Сумма снятия должна быть положительной")
        else:
            self.balance -= amount
            print(f"Успешно снято {amount}. Остаток: {self.balance}")

    def __str__(self):
        return f"Счет №{self.account_number}, баланс: {self.balance}"

account = BankAccount("123456789", 1000)
print(account)

account.deposit(500)
account.deposit(-200)
account.withdraw(200)
account.withdraw(2000)
account.withdraw(-100)