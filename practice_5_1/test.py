import math

import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x ** 2)


def lagrange_interpolation(x, x_nodes, y_nodes):
    result = 0
    for i in range(len(x_nodes)):
        temp = y_nodes[i]
        for j in range(len(x_nodes)):
            if i != j:
                temp *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += temp
    return result


a = -1
b = 1
n = 10

x_nodes = [math.cos(((2 * i + 1) * math.pi) / (2 * n)) for i in range(n - 1)]
x_nodes_inter = [a + i * (b - a) / 100 for i in range(101)]

y_nodes = [f(x) for x in x_nodes]
y_inter = [lagrange_interpolation(x, x_nodes, y_nodes) for x in x_nodes_inter]
plt.figure(figsize=(10, 6))
plt.plot(x_nodes_inter, [f(x) for x in x_nodes_inter], label='f(x)', color='blue', linewidth=2)
plt.scatter(x_nodes, y_nodes, color='red', label='Чебушевские узлы', zorder=5)
plt.plot(x_nodes_inter, y_inter, label='Интерполяционный полином', color='green', linestyle='--')
plt.title('Интерполяция Лагранжа')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
