while True:
    data = []
    print("Вводите элементы последовательности (Enter для обработки):")
    while True:
        item = input('> ')
        if item == '':
            if data:
                unique_data = list(dict.fromkeys(data))
                print("Уникальные элементы:", unique_data)
                break
        data.append(item)
    
    choice = input("Завершить программу? (Y/N): ").strip().lower()
    if choice == 'y':
        break