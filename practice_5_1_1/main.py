import math
import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x ** 2)


def chebyshev_nodes(n):
    return [math.cos((2 * i + 1) * math.pi / (2 * n)) for i in range(n)]


def equidistant_nodes(n, a, b):
    return [a + i * (b - a) / (n - 1) for i in range(n)]


def lagrange_interpolation(x, x_nodes, y_nodes):
    result = 0
    for i in range(len(x_nodes)):
        temp = y_nodes[i]
        for j in range(len(x_nodes)):
            if i != j:
                temp *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += temp
    return result


def plot_interpolation(a, b, n):
    x_nodes_eq = equidistant_nodes(n, a, b)
    y_nodes_eq = [f(x) for x in x_nodes_eq]

    x_nodes_cheb = chebyshev_nodes(n)
    y_nodes_cheb = [f(x) for x in x_nodes_cheb]

    x_nodes_inter = [a + i * (b - a) / 100 for i in range(101)]

    y_inter_eq = [lagrange_interpolation(
        x, x_nodes_eq, y_nodes_eq) for x in x_nodes_inter]

    y_inter_cheb = [lagrange_interpolation(
        x, x_nodes_cheb, y_nodes_cheb) for x in x_nodes_inter]

    plt.figure(figsize=(12, 8))
    plt.plot(x_nodes_inter, [f(x) for x in x_nodes_inter],
             label='f(x)', color='blue', linewidth=2)
    plt.scatter(x_nodes_eq, y_nodes_eq, color='red',
                label='Равностоящие узлы', zorder=5)
    plt.plot(x_nodes_inter, y_inter_eq, label='Интерполяционный полином (равностоящие узлы)',
             color='green', linestyle='solid')
    plt.scatter(x_nodes_cheb, y_nodes_cheb, color='orange',
                label='Чебышёвские узлы', zorder=5)
    plt.plot(x_nodes_inter, y_inter_cheb,
             label='Интерполяционный полином (Чебышёвские узлы)', color='purple', linestyle='--')
    plt.title('Интерполяция Лагранжа: Равностоящие и Чебышёвские узлы')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()


a = -1
b = 1
n = 10
plot_interpolation(a, b, n)
