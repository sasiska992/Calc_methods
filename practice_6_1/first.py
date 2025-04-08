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


def main():
    x_nodes = [i / 10 for i in range(21)]
    summ = 0
    print("Метод левых прямоугольников".center(80))
    table = PrettyTable(["x", "erf(x)", "∫f(x)", "Δ(erf(x) - ∫f(x))"])
    temp = 0
    for i in range(len(x_nodes) - 1):
        temp += math.erf(x_nodes[i + 1])
        summ += left_rectangles(x_nodes[i], x_nodes[i + 1])
        table.add_row([f"{x_nodes[i]} - {x_nodes[i + 1]}", math.erf(x_nodes[i + 1]), summ,
                      abs(math.erf(x_nodes[i]) - summ)])
    print(table)

    table = PrettyTable(["Суммарное значение erf(x)",
                        "Cумарное значение ∫f(x)", "Суммарное отклонение"])
    table.add_row([temp, summ, abs(summ - temp)])
    print(table)
    print("\n")

    summ = 0
    print("Метод средних прямоугольников".center(80))
    table = PrettyTable(["x", "erf(x)", "∫f(x)", "Δ(erf(x) - ∫f(x))"])
    temp = 0
    for i in range(len(x_nodes) - 1):
        summ += middle_rectangles(x_nodes[i], x_nodes[i + 1])
        temp += math.erf(x_nodes[i + 1])
        table.add_row([f"{x_nodes[i]} - {x_nodes[i + 1]}", math.erf(x_nodes[i + 1]), summ,
                      abs(math.erf(x_nodes[i]) - summ)])
    print(table)
    table = PrettyTable(["Суммарное значение erf(x)",
                        "Cумарное значение ∫f(x)", "Суммарное отклонение"])
    table.add_row([temp, summ, abs(summ - temp)])
    print(table)
    print("\n")

    summ = 0
    print("Метод правых прямоугольников".center(80))
    table = PrettyTable(["x", "erf(x)", "∫f(x)", "Δ(erf(x) - ∫f(x))"])
    temp = 0
    for i in range(len(x_nodes) - 1):
        temp += math.erf(x_nodes[i + 1])
        summ += right_rectangles(x_nodes[i], x_nodes[i + 1])
        table.add_row([f"{x_nodes[i]} - {x_nodes[i + 1]}", math.erf(x_nodes[i + 1]), summ,
                      abs(math.erf(x_nodes[i]) - summ)])
    print(table)

    table = PrettyTable(["Суммарное значение erf(x)",
                        "Cумарное значение ∫f(x)", "Суммарное отклонение"])
    table.add_row([temp, summ, abs(summ - temp)])
    print(table)


if __name__ == "__main__":
    main()
