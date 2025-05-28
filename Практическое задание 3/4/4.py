mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Вся матрица:", ', '.join([', '.join(map(str, row)) for row in mat]))

print("\nПо строкам:")
for i, row in enumerate(mat, 1):
    print(f"{i} строка: {', '.join(map(str, row))}")

print("\nПо элементам:")
for i, row in enumerate(mat, 1):
    for j, element in enumerate(row, 1):
        print(f"Элемент ({i},{j}): {element}")