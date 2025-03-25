import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_nodes = [2, 3, 5, 7]
y_nodes = [4, -2, 6, -3]

cs = CubicSpline(x_nodes, y_nodes)

x = [i / 10 for i in range(20, 71)]
y_spline = [cs(xi) for xi in x]

# Интерполяции в узловых точках
interpolated_values = [cs(xi) for xi in x_nodes]

# Результаты интерполяции в узловых точках
for xi, yi in zip(x_nodes, interpolated_values):
    print(f"f({xi}) = {yi}")

plt.figure(figsize=(10, 6))
plt.plot(x, y_spline, label='Кубический сплайн', color='blue')
plt.scatter(x_nodes, y_nodes, color='red', label='Узловые точки')
plt.title('Кубический сплайн для заданной таблицы')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
