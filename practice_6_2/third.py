import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math


def f(x, r):
    return x + r ** 2


def print_graphic(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.gca().set_aspect('equal')  # Установка равного масштаба по осям
    plt.title('Окружность')
    plt.grid()
    plt.show()


def task_1():
    n = 5
    x_values = []
    y_values = []
    for angle in range(0, 361):  # от 0 до 360 градусов
        radians = math.radians(angle)  # преобразование градусов в радианы
        x_values.append(n * math.cos(radians))
        y_values.append(n * math.sin(radians))

    a = 2 * n
    b = 2 * n
    print(f"Прямоугольник размером {a} × {
    b}, в котором целиком находится фигура\n\n")
    return x_values, y_values


def bobr_kurva(x_values, y_values):
    n = 200
    mini_x, maxi_x = min(x_values), max(x_values)
    random_dots = [{
        "x": random.uniform(mini_x, maxi_x),
        "y": random.uniform(mini_x, maxi_x)
    } for _ in range(n)]
    m = 0
    for temp_dict in random_dots:
        x = temp_dict["x"]
        y = temp_dict["y"]
        # if (x + 5) ** 2 + (y - 5) ** 2 < 5 ** 2:
        if x ** 2 + y ** 2 < 5 ** 2:
            m += 1
    pi = 4 * m / n
    print(pi, "Примерное число pi")
    print(f"{m} из {n} точек находятся в окружности")
    return m


def main():
    x_values, y_values = task_1()
    m = bobr_kurva(x_values, y_values)

    print_graphic(x_values, y_values)


if __name__ == "__main__":
    main()
