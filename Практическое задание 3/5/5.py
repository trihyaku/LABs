def input_matrix():
    matrix = []
    print("Вводите строки матрицы (числа через запятую, Enter для завершения):")
    while True:
        row_input = input("> ").strip()
        if not row_input:
            break
        try:
            row = [int(x.strip()) for x in row_input.split(',')]
            if matrix and len(row) != len(matrix[0]):
                print(f"Ошибка: должно быть {len(matrix[0])} элементов в строке")
                continue
            matrix.append(row)
        except ValueError:
            print("Ошибка: вводите только числа, разделенные запятыми")
    return matrix

def matrix_addition(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Ошибка: матрицы должны быть одинакового размера")
        return None
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_scalar_multiplication(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]

def matrix_multiplication(a, b):
    if len(a[0]) != len(b):
        print("Ошибка: количество столбцов первой матрицы должно равняться количеству строк второй")
        return None
    
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

print("Первая матрица\n")
mat1 = input_matrix()
print("Вторая матрица\n")
mat2 = input_matrix()

print("\nСумма матриц:")
print(matrix_addition(mat1, mat2))

print("\nУмножение первой матрицы на 2:")
print(matrix_scalar_multiplication(mat1, 2))

print("\nПроизведение матриц:")
print(matrix_multiplication(mat1, mat2))