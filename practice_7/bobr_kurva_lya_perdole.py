import math
import time

from prettytable import PrettyTable


def f(t):
    return (2 / math.sqrt(math.pi)) * math.e ** (-t ** 2)


def middle_rectangles(a, b, func):
    return (b - a) * func((a + b) / 2)


def left_rectangles(a, b, func):
    return func(a) * (b - a)


def right_rectangles(a, b, func):
    return func(b) * (b - a)


def print_table(x_nodes, title, func, f):
    # print(title.center(80))
    table = PrettyTable(["x", "erf(x)", "∫f(x)", "Отклонение"])
    start = time.time()
    temp = 0
    summ = 0
    summ_summ = 0
    for i in range(len(x_nodes) - 1):
        erf = math.erf(x_nodes[i + 1])
        temp += erf
        summ += abs(func(x_nodes[i], x_nodes[i + 1], f))
        summ_summ += summ
        table.add_row([f"{x_nodes[i]} - {x_nodes[i + 1]}",
                       erf, summ, abs(erf - summ)])
    end = time.time()
    # print(table)
    # table = PrettyTable(["Суммарное значение erf(x)",
    #                      "Cумарное значение ∫f(x)", "Суммарное отклонение", "Время выполнения программы"])
    # table.add_row([temp, summ_summ, abs(summ_summ - temp), end - start])
    # print(table)
    # print("\n")
    # return f"Время выполнения программы для {title} составило: {end - start}"
    return end - start


def main(f):
    x_nodes = [i / 10 for i in range(21)]
    print(print_table(x_nodes, "Метод левых прямоугольников", left_rectangles, f))
    print(print_table(x_nodes, "Метод средних прямоугольников", middle_rectangles, f))
    print(print_table(x_nodes, "Метод правых прямоугольников", right_rectangles, f))


if __name__ == "__main__":
    main(f)
