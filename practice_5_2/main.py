import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable


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
        decimal_part = ''.join(superscripts.get(digit, digit)
                               # Берем только два знака
                               for digit in parts[1][:2])
        # Используем верхнюю точку (U+00B7)
        return f"{whole_part}·{decimal_part}"

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
        [sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]),
         sum([x_nodes[i] * y_nodes[i] for i in range(n)])],
        [sum([x for x in x_nodes]), n, sum([y for y in y_nodes])]
    ]
    a, b = gauss(matrix)
    a = round(a, 2)
    b = round(b, 2)
    if b < 0:
        return f"y = {a}•x - {abs(b)}", a, b
    return f"y = {a}•x + {b}", a, b


def second():
    matrix = [
        [sum([ln(x) ** 2 for x in x_nodes]), sum([ln(x) for x in x_nodes]),
         sum([ln(x_nodes[i]) * ln(y_nodes[i]) for i in range(n)])],
        [sum([ln(x) for x in x_nodes]), n, sum([ln(y) for y in y_nodes])]
    ]
    a, b = gauss(matrix)
    a = round(a, 2)
    b = math.e ** b
    b = round(b, 2)
    return f"y = {b}•x{superscript(a)}", a, b


def third():
    matrix = [
        [sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]),
         sum([x_nodes[i] * ln(y_nodes[i]) for i in range(n)])],
        [sum([x for x in x_nodes]), n, sum([ln(y) for y in y_nodes])]
    ]
    a, b = gauss(matrix)
    a = round(a, 2)
    b = math.e ** b
    b = round(b, 2)
    return f"y = {b}•e{superscript(a)}x", a, b


def fourth():
    matrix = [
        [sum([x ** 4 for x in x_nodes]), sum([x ** 3 for x in x_nodes]), sum([x **
                                                                              2 for x in x_nodes]), sum([x_nodes[i] ** 2 * y_nodes[i] for i in range(n)])],
        [sum([x ** 3 for x in x_nodes]), sum([x ** 2 for x in x_nodes]),
         sum([x for x in x_nodes]), sum([x_nodes[i] * y_nodes[i] for i in range(n)])],
        [sum([x ** 2 for x in x_nodes]), sum([x for x in x_nodes]),
         n, sum([y_nodes[i] for i in range(n)])],
    ]
    a, b, c = gauss(matrix)
    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)
    if b < 0:
        if c < 0:
            return f"y = {a}x² - {abs(b)}x - {abs(c)}", a, b, c
        return f"y = {a}x² - {abs(b)}x + {c}", a, b, c
    if c < 0:
        return f"y = {a}x² + {b}x - {abs(c)}", a, b, c
    return f"y = {a}x² + {b}x + {c}", a, b, c


x_nodes = [2, 6, 10, 14, 18, 22]
y_nodes = [3.1, 6.7, 9.5, 11.9, 14, 15.5]
n = len(x_nodes)


def create_graphic():
    # x_values = [i / 10 for i in range(x_nodes[0] * 10, x_nodes[-1] * 10)]
    # a, b = list(first()[1:])
    # y_1_nodes = [a * x + b for x in x_values]
    #
    # a, b = list(second()[1:])
    # y_2_nodes = [b * x ** a for x in x_values]
    #
    # a, b = list(third()[1:])
    # y_3_nodes = [b * math.e ** (a * x) for x in x_values]
    #
    # a, b, c = list(fourth()[1:])
    # y_4_nodes = [a * x ** 2 + b * x + c for x in x_values]
    #
    # plt.scatter(x_nodes, y_nodes)
    # plt.plot(x_values, y_1_nodes, label=first()[0])
    # plt.plot(x_values, y_2_nodes, label=second()[0])
    # plt.plot(x_values, y_3_nodes, label=third()[0])
    # plt.plot(x_values, y_4_nodes, label=fourth()[0])

    a, b = list(first()[1:])
    y_1_nodes = [a * x + b for x in x_nodes]

    a, b = list(second()[1:])
    y_2_nodes = [b * x ** a for x in x_nodes]

    a, b = list(third()[1:])
    y_3_nodes = [b * math.e ** (a * x) for x in x_nodes]

    a, b, c = list(fourth()[1:])
    y_4_nodes = [a * x ** 2 + b * x + c for x in x_nodes]
    plt.scatter(x_nodes, y_nodes)
    plt.plot(x_nodes, y_1_nodes, label=first()[0])
    plt.plot(x_nodes, y_2_nodes, label=second()[0])
    plt.plot(x_nodes, y_3_nodes, label=third()[0])
    plt.plot(x_nodes, y_4_nodes, label=fourth()[0])

    table = PrettyTable(["Функция", "Δy"])
    table.add_row(
        ["Линейная", sum([(y[0] - y[1]) ** 2 for y in zip(y_nodes, y_1_nodes)])])
    table.add_row(
        ["Степенная", sum([(y[0] - y[1]) ** 2 for y in zip(y_nodes, y_2_nodes)])])
    table.add_row(["Показательная", sum(
        [(y[0] - y[1]) ** 2 for y in zip(y_nodes, y_3_nodes)])])
    table.add_row(["Квадратичная", sum(
        [(y[0] - y[1]) ** 2 for y in list(zip(y_nodes, y_4_nodes))])])
    print(table)
    plt.legend()
    plt.show()


def main():
    print("Первый номер\n".center(50))
    print(first()[0] + "\n")
    print("=================================".center(50))

    print("Второй номер\n".center(50))
    print(second()[0] + "\n")
    print("=================================".center(50))

    print("Третий номер\n".center(50))
    print(third()[0] + "\n")
    print("=================================".center(50))

    print("Четвертый номер\n".center(50))
    print(fourth()[0] + "\n")
    print("=================================".center(50))

    create_graphic()


main()
