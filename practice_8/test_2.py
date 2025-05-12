import math
import cmath
from prettytable import PrettyTable


def solve_specific_cubic(alpha):
    """Решает уравнение x³ + 3x² + α²x + 3α² = 0 методом Кардано"""
    p = alpha ** 2 - 3
    q = 2 * alpha ** 2 - 2

    discriminant = (q / 2) ** 2 + (p / 3) ** 3

    # Проверяем тип дискриминанта перед сравнением
    if isinstance(discriminant, complex) or discriminant > 0:
        # Один действительный и два комплексных корня
        s = cmath.sqrt(discriminant)
        u = (-q / 2 + s) ** (1 / 3)
        v = (-q / 2 - s) ** (1 / 3)
        y1 = u + v
        x1 = y1 - 1  # Обратная подстановка x = y - 1

        # Находим остальные корни через деление многочлена
        b_new = 3 + 1 * x1
        c_new = alpha ** 2 + b_new * x1
        quadratic_discriminant = b_new ** 2 - 4 * 1 * c_new

        if quadratic_discriminant >= 0:
            x2 = (-b_new + math.sqrt(quadratic_discriminant)) / 2
            x3 = (-b_new - math.sqrt(quadratic_discriminant)) / 2
            return [x1, x2, x3]
        else:
            x2 = (-b_new + cmath.sqrt(quadratic_discriminant)) / 2
            x3 = (-b_new - cmath.sqrt(quadratic_discriminant)) / 2
            return [x1, x2, x3]

    elif abs(discriminant) < 1e-10:  # Практически нуль
        # Два действительных корня (один кратный)
        y1 = -2 * (q / 2) ** (1 / 3)
        y2 = (q / 2) ** (1 / 3)
        x1 = y1 - 1
        x2 = y2 - 1
        return [x1, x2]
    else:
        # Три действительных корня
        r = cmath.sqrt(-(p ** 3) / 27)
        theta = cmath.acos(-q / (2 * r))
        y1 = 2 * abs(r) ** (1 / 3) * cmath.cos(theta / 3)
        y2 = 2 * abs(r) ** (1 / 3) * cmath.cos((theta + 2 * cmath.pi) / 3)
        y3 = 2 * abs(r) ** (1 / 3) * cmath.cos((theta + 4 * cmath.pi) / 3)
        x1 = y1 - 1
        x2 = y2 - 1
        x3 = y3 - 1
        return [x1, x2, x3]


def format_root(root):
    """Форматирует корень для вывода"""
    if isinstance(root, complex):
        if abs(root.imag) < 1e-10:
            return f"{root.real:.3f}"
        if root.imag > 0:
            return f"{root.real:.3f}+{root.imag:.3f}i"
        return f"{root.real:.3f}{root.imag:.3f}i"
    return f"{root:.3f}"


# Создаем таблицу для вывода
table = PrettyTable()
table.field_names = ["α", "Корни уравнения"]

# Тестируем для разных значений α
test_alphas = [0.1, 1, 3, 10, 100]

for alpha in test_alphas:
    roots = solve_specific_cubic(alpha)
    table.add_row([alpha, ", ".join(format_root(root) for root in roots)])

print("Решение уравнения x³ + 3x² + α²x + 3α² = 0")
print(table)
