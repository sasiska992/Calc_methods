import math
from prettytable import PrettyTable


def solve_cubic_cardano(a, b, c, d):
    b1 = c / a
    c1 = d / a
    d1 = 0
    p = c1 - (b1 ** 2) / 3
    q = d1 - (b1 * c1) / 3 + 2 * (b1 ** 3) / 27

    discriminant = (q / 2) ** 2 + (p / 3) ** 3

    if discriminant > 0:
        s = math.sqrt(discriminant)
        y1 = (-q / 2 + s) ** (1 / 3) + (-q / 2 - s) ** (1 / 3)
        x1 = y1 - b1 / 3
        return [x1]
    elif discriminant == 0:
        y1 = -2 * (q / 2) ** (1 / 3)
        y2 = (q / 2) ** (1 / 3)
        x1 = y1 - b1 / 3
        x2 = y2 - b1 / 3
        return [x1, x2]
    else:
        r = math.sqrt(-(p ** 3) / 27)
        theta = math.acos(-q / (2 * r))
        y1 = 2 * math.pow(r, 1 / 3) * math.cos(theta / 3)
        y2 = 2 * math.pow(r, 1 / 3) * math.cos((theta + 2 * math.pi) / 3)
        y3 = 2 * math.pow(r, 1 / 3) * math.cos((theta + 4 * math.pi) / 3)
        x1 = y1 - b1 / 3
        x2 = y2 - b1 / 3
        x3 = y3 - b1 / 3
        return [x1, x2, x3]


def format_complex_number(num):
    if isinstance(num, complex):
        if num.imag >= 0:
            return f"{round(num.real, 3)} + {round(num.imag, 3)}i"
        else:
            return f"{round(num.real, 3)} - {round(abs(num.imag), 3)}i"
    return f"{round(num, 3)}"


def solve_cubic_newton(a, b, c, d, x0, max_iter=100):
    def f(x):
        return a * x ** 3 + b * x ** 2 + c * x + d

    def df(x):
        return 3 * a * x ** 2 + 2 * b * x + c

    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < -10 ** 6:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx / dfx
    return x


cardano_table = PrettyTable()
cardano_table.field_names = ["α", "Корни (метод Кардано)"]

newton_table = PrettyTable()
newton_table.field_names = ["α", "Начальное приближение", "Корень (метод Ньютона)"]

a_values = [3, 10, 100, 10 ** 6]
initial_guesses = [-1, -10, -100, -10 ** 6]

for a, x0 in zip(a_values, initial_guesses):
    roots = solve_cubic_cardano(1, 3, a ** 2, 3 * a ** 2)
    formatted_roots = [format_complex_number(root) for root in roots]
    cardano_table.add_row([a, ", ".join(formatted_roots)])

    root = solve_cubic_newton(1, 3, a ** 2, 3 * a ** 2, x0)
    newton_table.add_row([a, x0, format_complex_number(root)])

print("Метод Кардано для уравнения x³ + 3x² + α²x + 3α² = 0")
print(cardano_table)

print("\nМетод Ньютона для уравнения x³ + 3x² + α²x + 3α² = 0")
print(newton_table)
