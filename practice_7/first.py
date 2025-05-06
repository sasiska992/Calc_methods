import math
from bobr_kurva_lya_perdole import print_table, middle_rectangles
import time

from prettytable import PrettyTable


def f(x):
    return (2 / math.sqrt(math.pi)) * math.exp(-(x**2))


def func(h, x_start, y_start, x_end):
    x = x_start
    y = y_start

    while x < x_end:
        r1 = h * f(x)
        r2 = h * f(x + h / 2)
        r3 = h * f(x + h / 2)
        r4 = h * f(x + h)
        x += h
        y += (r1 + r2 * 2 + r3 * 2 + r4) / 6
    return y


def main(x_values):
    x_start = 0
    y_start = 0
    table = PrettyTable(["x", "y`", "erf(x)", "Разница"])
    start = time.time()
    for i in range(len(x_values)):
        a = func(0.1, x_start, y_start, x_values[i])
        b = math.erf(x_values[i])
        table.add_row([x_values[i], a, b, abs(a - b)])

    end = time.time()
    print(table)
    return end - start


if __name__ == "__main__":
    x_values = [i / 10 for i in range(0, 21)]
    time_table = PrettyTable(["ОДУ", "Метод средних прямоугольников", "Разница"])
    odu = main(x_values)
    middle = print_table(x_values, "", middle_rectangles, f)
    time_table.add_row([odu, middle, abs(middle - odu)])
    print(time_table)
