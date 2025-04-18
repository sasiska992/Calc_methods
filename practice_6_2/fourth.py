import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math

n = 5
A = 11 + n
B = 11 - n


def rho(phi):
    return math.sqrt(A * math.cos(phi) ** 2 + B * math.sin(phi) ** 2)


def print_graphic(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.gca().set_aspect('equal')  # Установка равного масштаба по осям
    plt.title('Окружность')
    plt.grid()
    plt.show()


def task_1():
    num_points_plot = 1000
    phi_list = [2 * math.pi * i /
                num_points_plot for i in range(num_points_plot)]

    r_list = [rho(phi) for phi in phi_list]

    x_values = [r * math.cos(phi) for r, phi in zip(r_list, phi_list)]
    y_values = [r * math.sin(phi) for r, phi in zip(r_list, phi_list)]
    a = max(x_values) + abs(min(x_values))
    b = round(max(y_values) + abs(min(y_values)), 3)
    print(f"Прямоугольник размером {a} × {
          b}, в котором целиком находится фигура\n\n")
    return x_values, y_values


def bobr_kurva(x_values, y_values):
    n = 100
    mini_x, maxi_x = min(x_values), max(x_values)
    mini_y, maxi_y = min(y_values), max(y_values)
    random_dots = [{
        "x": random.uniform(mini_x, maxi_x),
        "y": random.uniform(mini_y, maxi_y)
    } for _ in range(n)]
    m = 0
    for temp_dict in random_dots:
        x = temp_dict["x"]
        y = temp_dict["y"]
        if x > 0:
            phi = math.atan(y / x)
        elif x < 0:
            phi = math.pi + math.atan(y / x)
        elif x == 0 and y > 0:
            phi = math.py / 2
        elif x == 0 and y < 0:
            phi = - math.py / 2
        elif x == 0 and y == 0:
            phi = 0
    pi = 4 * m / n
    print(pi, "Примерное число pi")
    return m


def main():
    x_values, y_values = task_1()
    # m = bobr_kurva(x_values, y_values)
    # print(m)

    print_graphic(x_values, y_values)


if __name__ == "__main__":
    main()
