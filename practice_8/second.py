import math
import cmath
from prettytable import PrettyTable
import numpy as np


def solve_cubic_cardano(a, b, c):
    p = b - (a**2) / 3
    q = c - a * b / 3 + 2 * (a / 3) ** 3

    discriminant = (q / 2) ** 2 + (p / 3) ** 3

    s = math.sqrt(discriminant)
    y1 = np.cbrt(-q / 2 + s) + np.cbrt(-q / 2 - s)
    x1 = y1 - a / 3
    return [int(x1)]


def find_other_roots(a, b, c, root):
    b_new = b + a * root
    c_new = c + b_new * root

    disc = b_new**2 - 4 * a * c_new

    sqrt_disc = cmath.sqrt(disc)

    x2 = format_complex_number(complex((-b_new + sqrt_disc) / (2 * a)))
    x3 = format_complex_number(complex((-b_new - sqrt_disc) / (2 * a)))

    return [root, x2, x3]


def format_complex_number(num):
    if isinstance(num, complex):
        if num.real == 0:
            if num.imag >= 0:
                return f"{round(num.imag, 3)}i"
            else:
                return f"- {round(abs(num.imag), 3)}i"
        else:
            if num.imag >= 0:
                return f"{round(num.real, 3)} + {round(num.imag, 3)}i"
            else:
                return f"{round(num.real, 3)} - {round(abs(num.imag), 3)}i"
    return f"{round(num, 3)}"


def solve_cubic_newton(a, b, c, x0, max_iter=100):
    def f(x):
        return x**3 + a * x**2 + b * x + c

    def df(x):
        return 3 * x**2 + 2 * a * x + b

    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < -(10**6):
            return [x]
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx / dfx
    return [x]


cardano_table = PrettyTable()
cardano_table.field_names = ["α", "Корни (метод Кардано)"]

newton_table = PrettyTable()
newton_table.field_names = ["α", "Начальное приближение", "Корень (метод Ньютона)"]

# x**3 + 3x**2 + 9x + 27 = 0
# x**3 + 3x**2 + 100x + 300 = 0
a_values = [3, 10, 100, 10**27]
initial_guesses = [-1, -10, -100, -(10**6)]

for a, x0 in zip(a_values, initial_guesses):
    roots = solve_cubic_cardano(3, a**2, 3 * a**2)
    roots += find_other_roots(1, 3, a**2, roots[0])
    roots = list(set(roots))
    result = ""
    for i in range(len(roots)):
        result += f"{roots[i]}, "
    cardano_table.add_row([a, result])

    roots = solve_cubic_newton(3, a**2, 3 * a**2, x0)
    roots += find_other_roots(1, 3, a**2, roots[0])
    roots = list(set(roots))
    result = ""
    for i in range(len(roots)):
        result += f"{roots[i]}, "
    newton_table.add_row([a, x0, result])

print("Метод Кардано для уравнения x³ + 3x² + α²x + 3α² = 0")
print(cardano_table)

print("\nМетод Ньютона для уравнения x³ + 3x² + α²x + 3α² = 0")
print(newton_table)
