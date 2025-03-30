import math


def superscript(n):
    superscripts = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    # Преобразуем число в строку и разбиваем на целую и дробную части
    parts = str(n).split('.')

    # Обрабатываем целую часть
    whole_part = ''.join(superscripts.get(digit, digit) for digit in parts[0])

    # Обрабатываем дробную часть, если она есть
    if len(parts) > 1:
        decimal_part = ''.join(superscripts.get(digit, digit) for digit in parts[1][:2])  # Берем только два знака
        return f"{whole_part}·{decimal_part}"  # Используем верхнюю точку (U+00B7)

    return whole_part


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


def ln(value):
    return math.log(value, math.e)


def first():
    matrix = [
        [sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]), sum([x_nodes[i] * y_nodes[i] for i in range(n)])],
        [sum([x for x in x_nodes]), n, sum([y for y in y_nodes])]
    ]
    a, b = gauss(matrix)
    a = round(a, 2)
    b = round(b, 2)
    if b < 0:
        return f"y = {a}•x - {abs(b)}"
    return f"y = {a}•x - {b}"


def second():
    matrix = [
        [sum([ln(x) ** 2 for x in x_nodes]), sum([ln(x) for x in x_nodes]), sum([ln(x_nodes[i]) * ln(y_nodes[i]) for i in range(n)])],
        [sum([ln(x) for x in x_nodes]), n, sum([ln(y) for y in y_nodes])]
    ]
    a, b = gauss(matrix)
    a = round(a, 2)
    b = math.e ** b
    b = round(b, 2)
    return f"y = {b}•x{superscript(a)}"


def third():
    matrix = [
        [sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]), sum([x_nodes[i] * ln(y_nodes[i]) for i in range(n)])],
        [sum([x for x in x_nodes]), n, sum([ln(y) for y in y_nodes])]
    ]
    a, b = gauss(matrix)
    a = round(a, 2)
    b = math.e ** b
    b = round(b, 2)
    return f"y = {b}•e{superscript(a)}x"


def fourth():
    matrix = [
        [sum([x ** 4 for x in x_nodes]), sum([x ** 3 for x in x_nodes]), sum([x ** 2 for x in x_nodes]), sum([x_nodes[i] ** 2 * y_nodes[i] for i in range(n)])],
        [sum([x ** 3 for x in x_nodes]), sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]), sum([x_nodes[i] * y_nodes[i] for i in range(n)])],
        [sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]), n, sum([y_nodes[i] for i in range(n)])],
    ]
    a, b, c = gauss(matrix)
    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)
    return f"y = {a}x² + {b}x + {c}"


x_nodes = [2, 5, 8, 11, 14, 17]
y_nodes = [2.1, 3.4, 4.2, 4.6, 5.2, 5.4]
n = len(x_nodes)


def main():
    print("Первый номер\n".center(50))
    print(first() + "\n")
    print("=================================".center(50))

    print("Второй номер\n".center(50))
    print(second() + "\n")
    print("=================================".center(50))

    print("Третий номер\n".center(50))
    print(third() + "\n")
    print("=================================".center(50))

    print("Четвертый номер\n".center(50))
    print(fourth())
    print("=================================".center(50))


main()
