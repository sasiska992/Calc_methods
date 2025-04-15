
import matplotlib.pyplot as plt


def f(x, n):
    if 0 <= x < n:
        return 10 * x / n
    elif n <= x < 20:
        return 10 * ((x - 20) / n - 20)
    else:
        return None


def main():
    n = 5
    x_values = list(range(20))
    y_values = []
    i = 0
    while i < len(x_values):
        x = x_values[i]
        y_x = f(x, n)
        if y_x >= 0:
            y_values.append(y_x)
            i += 1
        else:
            del x_values[i]

    # Построение графика
    plt.plot(x_values, y_values, marker='o')
    plt.title('График функции f(x, n)')
    plt.xlabel('x')
    plt.ylabel('f(x, n)')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
