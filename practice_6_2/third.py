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


def bobr_kurva():
    n = 200
    radius = 5
    mini_x, maxi_x = -radius, radius  # Устанавливаем границы для генерации точек
    random_dots = [{
        "x": random.uniform(mini_x, maxi_x),
        "y": random.uniform(mini_x, maxi_x)
    } for _ in range(n)]

    m = 0
    inside_dots = []
    outside_dots = []

    for temp_dict in random_dots:
        x = temp_dict["x"]
        y = temp_dict["y"]
        if x ** 2 + y ** 2 < radius ** 2:  # Проверка, находится ли точка внутри окружности
            m += 1
            inside_dots.append(temp_dict)  # Сохраняем точки внутри окружности
        else:
            outside_dots.append(temp_dict)  # Сохраняем точки вне окружности

    pi = 4 * m / n
    print(pi, "Примерное число pi")
    print(f"{m} из {n} точек находятся в окружности")

    # Визуализация
    plt.figure(figsize=(radius, radius))

    # Рисуем окружность
    circle = plt.Circle((0, 0), radius, color='blue',
                        fill=False, linewidth=2, label='Окружность радиусом 5')
    plt.gca().add_artist(circle)

    # Рисуем случайные точки
    for dot in inside_dots:
        plt.scatter(dot["x"], dot["y"], color='red')  # Точки внутри окружности
    for dot in outside_dots:
        plt.scatter(dot["x"], dot["y"], color='green')  # Точки вне окружности

    plt.xlim(-radius - 1, radius + 1)
    plt.ylim(-radius - 1, radius + 1)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Случайные точки и окружность')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def main():
    x_values, y_values = task_1()
    # bobr_kurva(x_values, y_values)
    bobr_kurva()

    # print_graphic(x_values, y_values)


if __name__ == "__main__":
    main()
