import math
from prettytable import PrettyTable


def f(t):
    return (2/math.sqrt(math.pi)) * math.e**(-t**2)


def middle_rectangles(a, b):
    return (b - a) * f((a + b) / 2)


def left_rectangles(a, b):
    return f(a) * (b - a)


def right_rectangles(a, b):
    return f(b)*(b - a)


def print_table(x_nodes, title, func):
    print(title.center(80))
    table = PrettyTable(["x", "erf(x)", "∫f(x)", "Отклонение"])
    temp = 0
    summ = 0
    summ_summ = 0
    for i in range(len(x_nodes) - 1):
        erf = math.erf(x_nodes[i+1])
        temp += erf
        summ += abs(func(x_nodes[i], x_nodes[i + 1]))
        summ_summ += summ
        table.add_row([f"{x_nodes[i]} - {x_nodes[i + 1]}",
                      erf, summ, abs(erf - summ)])

    print(table)
    table = PrettyTable(["Суммарное значение erf(x)",
                        "Cумарное значение ∫f(x)", "Суммарное отклонение"])
    table.add_row([temp, summ_summ, abs(summ_summ - temp)])
    print(table)
    print("\n")
    return


def main():
    x_nodes = [i / 10 for i in range(4)]
    print_table(x_nodes, "Метод левых прямоугольников", left_rectangles)
    print_table(x_nodes, "Метод средних прямоугольников", middle_rectangles)
    print_table(x_nodes, "Метод правых прямоугольников", right_rectangles)


if __name__ == "__main__":
    main()
