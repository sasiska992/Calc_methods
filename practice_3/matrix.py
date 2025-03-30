import copy


def gauss(matrix):
    n = len(matrix)

    for i in range(n):
        # Поиск максимального элемента в текущем столбце
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Обмен текущей строки с строкой с максимальным элементом
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Проверка на вырожденность матрицы и наличия свободных переменных
        if abs(matrix[i][i]) < 1e-10:
            return None

        # Приведение к верхнетреугольному виду
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    # Обратный ход для нахождения решения
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n] / matrix[i][i]
        for k in range(i + 1, n):
            solution[i] -= (matrix[i][k] / matrix[i][i]) * solution[k]

    return solution


def get_identity(size):
    identity_matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        identity_matrix[i][i] = 1

    return identity_matrix


def inverse_matrix(input_matrix):
    matrix = copy.deepcopy(input_matrix)
    size = len(matrix)
    inverse = get_identity(size)

    for i in range(size):
        if matrix[i][i] == 0:
            k = i + 1
            while k < size and matrix[k][k] == 0:
                k += 1
            matrix[i], matrix[k] = matrix[k], matrix[i]
            inverse[i], inverse[k] = inverse[k], inverse[i]

        pivot = matrix[i][i]
        for j in range(size):
            matrix[i][j] /= pivot
            inverse[i][j] /= pivot

        for j in range(size):
            if i == j:
                continue
            factor = matrix[j][i]
            for k in range(size):
                matrix[j][k] -= factor * matrix[i][k]
                inverse[j][k] -= factor * inverse[i][k]

    return inverse


def norm(matrix):
    sums = []
    cols = len(matrix[0])

    for i in range(cols):
        sums.append(sum([abs(matrix[j][i]) for j in range(len(matrix))]))

    return max(sums)


def append_column(matrix, col):
    result = copy.deepcopy(matrix)

    for i in range(len(result)):
        result[i].append(col[i])

    return result


def multiply_by_vector(matrix, vector):
    result = []

    for i in range(len(matrix)):
        result.append(sum([matrix[i][j] * vector[j] for j in range(len(matrix[0]))]))

    return result


def sub(m1, m2):
    result = []

    for i in range(len(m1)):
        result.append([m1[i][j] - m2[i][j] for j in range(len(m1[0]))])

    return result
