import math
from first import middle_rectangles
from prettytable import PrettyTable


def f(x):
    '''
    func for second task
    '''
    return 4 / (1 + x**2)


def trapezoid(h_nodes, h):
    result = (f(h_nodes[0]) + f(h_nodes[-1])) / 2
    for i in range(1, len(h_nodes) - 1):
        result += f(h_nodes[i])
    result *= h
    return result


def rectangle(x_nodes, func, f):
    summ = 0
    for i in range(len(x_nodes) - 1):
        summ += func(x_nodes[i], x_nodes[i + 1], f)
    return summ


def main():
    a = 0
    b = 1
    n_values = [8, 32, 128, 512]

    table = PrettyTable(["n", "Метод трапеции", "Метод средних прямоугольников",
                         "Отклонение трапеции", "Отклонение прямоугольника"])
    for n in n_values:
        h_nodes = [i / n for i in range(a * n, b * n + 1)]
        result_trapeziod = trapezoid(h_nodes, 1/n)
        result_rectangle = rectangle(h_nodes, middle_rectangles, f)
        pi = math.pi
        table.add_row([n, result_trapeziod, result_rectangle,
                       abs(pi - result_trapeziod), abs(pi - result_rectangle)])
    print(table)


if __name__ == "__main__":
    main()
