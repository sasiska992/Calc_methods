import math
from prettytable import PrettyTable


def f(n):
    return 1 / (n ** 4 * (n ** 2 + 1))


def f2(n):
    return 1 / (n ** 2 + 1)


def compute_sum_with_error(func, error):
    k = 1
    new_value = func(k)
    result = 0
    while new_value > error:
        k += 1
        result += new_value
        new_value = func(k)

    return result, k


def main():
    result_table = PrettyTable(
        ["f(x)", "Кол-во членов 1 ряда", "f1(x)", "Кол-во членов 2 ряда", "Разница"])
    error = 10 ** -10
    first_res = compute_sum_with_error(f, error)
    first_ans = (math.pi ** 2) / 6 - (math.pi ** 4) / \
        90 + first_res[0]
    second_res = compute_sum_with_error(f2, error)
    result_table.add_row([first_ans, first_res[1], second_res[0],
                         second_res[1], abs(first_ans - second_res[0])])
    print(result_table)


main()
