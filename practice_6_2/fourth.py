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
    plt.gca().set_aspect('equal')
    plt.title(f'Фигура: A={A}, B={B}')
    plt.grid()
    plt.show()


def task_1():
    num_points_plot = 1000
    phi_list = [2 * math.pi * i /
                num_points_plot for i in range(num_points_plot)]

    r_list = [rho(phi) for phi in phi_list]

    x_values = [r * math.cos(phi) for r, phi in zip(r_list, phi_list)]
    y_values = [r * math.sin(phi) for r, phi in zip(r_list, phi_list)]
    return x_values, y_values


def bobr_kurva(x_values, y_values, num_points=1000):
    mini_x, maxi_x = min(x_values), max(x_values)
    mini_y, maxi_y = min(y_values), max(y_values)

    rect_area = (maxi_x - mini_x) * (maxi_y - mini_y)

    inside_count = 0
    inside_dots = []
    outside_dots = []

    for _ in range(num_points):
        x = random.uniform(mini_x, maxi_x)
        y = random.uniform(mini_y, maxi_y)

        r = math.sqrt(x ** 2 + y ** 2)
        if r == 0:
            phi = 0
        else:
            phi = math.atan2(y, x) % (2 * math.pi)

        if r <= rho(phi):
            inside_count += 1
            inside_dots.append((x, y))
        else:
            outside_dots.append((x, y))

    area = rect_area * inside_count / num_points

    plt.figure(figsize=(8, 8))

    plt.plot([mini_x, maxi_x, maxi_x, mini_x, mini_x], [mini_y, mini_y, maxi_y, maxi_y, mini_y], color='black', linestyle='--', label='Ограничивающий прямоугольник')

    theta = [i * 0.01 for i in range(628)]
    x_fig = [rho(t) * math.cos(t) for t in theta]
    y_fig = [rho(t) * math.sin(t) for t in theta]
    plt.plot(x_fig, y_fig, color='blue', label='Фигура')

    for dot in inside_dots:
        plt.scatter(dot[0], dot[1], color='red')
    for dot in outside_dots:
        plt.scatter(dot[0], dot[1], color='green')

    plt.xlim(mini_x - 1, maxi_x + 1)
    plt.ylim(mini_y - 1, maxi_y + 1)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Случайные точки и фигура')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    return area


def main():
    x_values, y_values = task_1()
    area = bobr_kurva(x_values, y_values)

    table = PrettyTable()
    table.field_names = ["Параметр", "Значение"]
    table.add_row(["Размер прямоугольника",
                   f"{round(max(x_values) - min(x_values), 3)} × {round(max(y_values) - min(y_values), 3)}"])
    table.add_row(["Приближенная площадь", f"{round(area, 3)}"])
    print(table)

    # print_graphic(x_values, y_values)


if __name__ == "__main__":
    main()
