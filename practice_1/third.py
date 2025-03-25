import time

from prettytable import PrettyTable


def first_func(k, x):
    return 1 / ((k ** 3 + x) ** 0.5)


def second_func(k, x):
    return 1 / ((k ** 3 - x) ** 0.5)


def mega_new_func(k, x):
    return ((k ** 3 - x) ** 0.5 - (k ** 3 + x) ** 0.5) / ((k ** 6 - x ** 2) ** 0.5)


def summ_func(x, func, check: bool = False, start=1, end=1):
    if not check:
        summ = 0
        k = 1
        current_value = func(k, x)
        while abs(current_value) >= 3 * 10 ** (-8):
            # print(k, current_value)
            summ += current_value
            k += 1
            current_value = func(k, x)
            # if abs(current_value < 3 * 10 ** -8):
            #     print(current_value)
        return summ, k

    summ = 0
    for k in range(start, end):
        current_value = func(k, x)
        # print(k, current_value)
        summ += current_value
    return summ, k - 1


def s_func(x):
    time_start = time.time()
    a, count_1 = summ_func(x, first_func)
    time_end = time.time()
    first_time = (time_end - time_start) * 1000

    time_start = time.time()
    b, count_2 = summ_func(x, second_func)
    time_end = time.time()
    second_time = (time_end - time_start) * 1000
    # print(a, b)
    return a - b, count_1, count_2, first_time, second_time


def main():
    result_table = PrettyTable(
        ["x", "s(x)", "Членов в первом ряду", "Членов во втором ряду", "Время первого ряда (мс)", "Время второго ряда (мс)", "Упрощённое выражение (значение)",
         "Упрощённое выражение (членов в ряду)"])
    for x in range(-9, 10):
        x /= 10
        result = s_func(x)
        new_func = summ_func(x, mega_new_func)
        result_table.add_row([x, result[0], result[1], result[2],
                             result[3], result[4], new_func[0], new_func[1]])
    print(result_table)


def check(func, start, end):
    value = summ_func(-0.9, func, check=True, start=start, end=end)
    for x in range(-9, 10):
        x /= 10
        prev_value = value
        print(prev_value[0] - value[0], end=",")
        value = summ_func(x, func)
    print()


if __name__ == '__main__':
    # print(s_func(0.5))
    # print(second_func(103576, 0.5) + first_func(103576, 0.5))
    # print(summ_func(0.5, first_func))
    # 1
    check(func=first_func, start=1000, end=1100)
    check(func=second_func, start=1000, end=1100)
    # 2, 3, 4
    main()
    # 5
    for x in [0.5, 0.999999999]:
        print(summ_func(x, first_func)[0] - summ_func(x, second_func)[0])
