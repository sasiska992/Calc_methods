import random

import matplotlib.pyplot as plt
from prettytable import PrettyTable


def f(x, n):
    if 0 <= x < n:
        return 10 * x / n
    elif n <= x < 20:
        return 10 * ((x - 20) / (n - 20))
    else:
        return None


def simson(x_nodes):
    result = f(x_nodes[0], 5) + f(x_nodes[-1], 5)
    temp_1, temp_2 = 0, 0
    for i in range(len(x_nodes)):
        if i % 2 == 0:
            temp_1 += f(x_nodes[i], 5)
        else:
            temp_2 += f(x_nodes[i], 5)
    result += temp_1 * 2 + temp_2 * 4
    aboba = ((x_nodes[-1] - x_nodes[0]) / len(x_nodes)) / 3

    result *= aboba
    return result


def print_graphic(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.title('График функции f(x, n)')
    plt.fill_between(x_values, y_values, color='skyblue', alpha=0.4)
    plt.xlabel('x')
    plt.ylabel('f(x, n)')
    plt.grid()
    plt.show()


def task_1():
    n = 5
    x_values = [i / 10 for i in range(200)]
    y_values = []
    for x in x_values:
        y_x = f(x, n)
        y_values.append(y_x)

    a = max(x_values)
    b = max(y_values)
    print(f"Прямоугольник размером {a} × {
          b}, в котором целиком находится фигура\n\n")
    return x_values, y_values


def task_2_3_4(x_values, y_values):
    n = 100
    a = max(x_values)
    b = max(y_values)

    # Генерация случайных точек
    random_dots = [{
        "x": random.uniform(0, a),
        "y": random.uniform(0, b)
    } for _ in range(n)]

    m = 0
    for temp_dict in random_dots:
        if temp_dict["y"] < f(temp_dict["x"], 5) and f(temp_dict["x"], 5) is not None:
            m += 1

    print(m, "- рандомных точек находится внутри фигуры")
    s = m / n * a * b
    print(s, "примерная площадь по этим точкам")

    real_s = a * b / 2
    simpson_s = simson(x_values)

    table = PrettyTable(["Аналитическое решение", "Метод Симпсона"])
    table.add_row([real_s, simpson_s])
    print(table)

    table = PrettyTable(
        ["Относительная погрешность", "Абсолютная погрешность"])
    table.add_row([round(abs(real_s - s), 3),
                  f"{round(abs(real_s - s) / s * 100, 3)}%"])
    print(table)

    # Визуализация
    plt.figure(figsize=(8, 8))

    # Рисуем фигуру
    x_fig = [x for x in x_values]
    y_fig = [f(x, 5) for x in x_fig]
    plt.plot(x_fig, y_fig, label='Фигура (ограниченная функцией f)', color='blue')

    # Заполнение области под фигурой
    plt.fill_between(x_fig, y_fig, color='blue', alpha=0.3)

    # Рисуем случайные точки
    for dot in random_dots:
        plt.scatter(dot["x"], dot["y"], color='red' if dot["y"]
                    < f(dot["x"], 5) else 'green')

    plt.xlim(0, a)
    plt.ylim(0, b)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Случайные точки и фигура')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


def main():
    x_values, y_values = task_1()
    task_2_3_4(x_values, y_values)
    # print_graphic(x_values, y_values)


if __name__ == "__main__":
    main()
