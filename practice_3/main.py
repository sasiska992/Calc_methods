import math
import matrix
from prettytable import PrettyTable


def part1():
    a = [
        [
            1.00,
            0.80,
            0.64,
        ],
        [
            1.00,
            0.90,
            0.81,
        ],
        [
            1.00,
            1.10,
            1.21,
        ],
    ]
    b = [math.erf(0.8), math.erf(0.9), math.erf(1.1)]
    m = matrix.append_column(a, b)

    t = PrettyTable(["x1", "x2", "x3", "cond", "residual"])

    row = []

    # Решения
    x = matrix.gauss(m)
    for i in range(len(x)):
        row.append(x[i])

    # Обусловленность
    norm = matrix.norm(a)
    norm_inverse = matrix.norm(matrix.inverse_matrix(a))
    cond = norm * norm_inverse
    row.append(cond)

    ax = matrix.multiply_by_vector(a, x)
    idk = [a - b for a, b in zip(ax, b)]
    residual = math.sqrt(sum([math.pow(a, 2) for a in idk]))

    row.append(residual)

    t.add_row(row)
    print(t)

    print("\n")

    t = PrettyTable(["x1 + x2 + x3", "erf(1.0)", "difference"])
    t.add_row([sum(x), math.erf(1.0), sum(x) - math.erf(1.0)])
    print(t)


def part2():
    a = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    b = [0.1, 0.3, 0.5]

    x = matrix.gauss(matrix.append_column(a, b))
    if x is None:
        print("Матрица имеет множество решений.")


# Пример использования
if __name__ == "__main__":
    print("Part 1:")
    part1()

    print()
    print("Part 2:")
    part2()
