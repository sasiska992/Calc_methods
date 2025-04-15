import math
from prettytable import PrettyTable


def f(x):
    if 0 <= x <= 2:
        return math.e ** (x ** 2)
    return 1 / (4 - math.sin(16 * math.pi * x))


def simson(x_nodes):
    result = f(x_nodes[0]) + f(x_nodes[-1])
    temp_1, temp_2 = 0, 0
    for i in range(len(x_nodes)):
        if i % 2 == 0:
            temp_1 += f(x_nodes[i])
        else:
            temp_2 += f(x_nodes[i])
    result += temp_1 * 2 + temp_2 * 4
    aboba = ((x_nodes[-1] - x_nodes[0]) / len(x_nodes)) / 3

    result *= aboba
    return result


def interpolation():
    pass


def main():
    a = 0
    b = 4

    table = PrettyTable(["n", "∫f(x)"])
    for i in range(1, 15):
        n = 2 ** i
        x_nodes = [i / n for i in range(a * n, b * n + 1)]
        table.add_row([n, simson(x_nodes)])
    print(table)


if __name__ == "__main__":
    main()
