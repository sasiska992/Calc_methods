import math
import matrix
from prettytable import PrettyTable


def solve_func(a: list[list[int]], b: list[int]):
    m = matrix.append_column(a, b)

    t = PrettyTable([*[f"x{i}" for i in range(len(b))], "Свободные члены",
                     "Результат подстановки", "Невязка"])

    row = []

    # Решения
    x = matrix.gauss(m)
    for i in range(len(x)):
        row.append(x[i])

    ax = matrix.multiply_by_vector(a, x)
    idk = [a - b for a, b in zip(ax, b)]
    residual = sum([math.pow(a, 2) for a in idk])
    row.append(b)
    row.append(ax)
    row.append(residual)
    t.add_row(row)
    print(t)


if __name__ == "__main__":
    print(" " * 30 + "Первое уравнение:")
    # solve_func(a=[
    #     [10**-4, 1],
    #     [1, 2]
    # ],
    #     b=[1, 4])
    #
    # solve_func(a=[
    #     [2.34, -4.21, -11.61],
    #     [8.04, 5.22, 0.27],
    #     [3.92, -7.99, 8.37]
    # ],
    #     b=[14.41, -6.44, 55.56])
    solve_func(a=[
        [12.14, 1.32, -0.78, -2.75],
        [-0.89, 16.75, 1.88, -1.55],
        [2.65, -1.27, -15.64, -0.64],
        [2.44, 1.52, 1.93, -11.43]
    ],
        b=[14.78, -12.14, -11.65, 4.26])
