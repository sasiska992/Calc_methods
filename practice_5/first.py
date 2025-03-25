import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x**2)


# Задаем отрезок
x = [i / 100 for i in range(-100, 101)]
y = [f(xi) for xi in x]

print(x)
print(y)

plt.figure(figsize=(12, 8))
plt.plot(x, y, label='f(x) = 1 / (1 + 25 * x^2)', color='blue')


# Настройки графика
plt.title('График функции и кубического сплайна')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
