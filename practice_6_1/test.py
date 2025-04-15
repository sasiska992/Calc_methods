import math


def create_spline(nodes_x, nodes_y):
    num_intervals = len(nodes_x) - 1
    intervals = [nodes_x[i + 1] - nodes_x[i] for i in range(num_intervals)]

    # Коэффициенты сплайна
    coeff_a = nodes_y[:-1]
    coeff_b = [0.0] * num_intervals
    coeff_d = [0.0] * num_intervals
    coeff_c = [0.0] * (num_intervals + 1)

    # Матрица для решения системы уравнений
    matrix_A = [[0.0] * (num_intervals + 1) for _ in range(num_intervals + 1)]
    vector_rhs = [0.0] * (num_intervals + 1)

    # Заполнение матрицы и правой части
    for i in range(1, num_intervals):
        matrix_A[i][i - 1] = intervals[i - 1]
        matrix_A[i][i] = 2.0 * (intervals[i - 1] + intervals[i])
        matrix_A[i][i + 1] = intervals[i]
        vector_rhs[i] = 3.0 * ((nodes_y[i + 1] - nodes_y[i]) / intervals[i] -
                               (nodes_y[i] - nodes_y[i - 1]) / intervals[i - 1])

    # Естественные граничные условия
    matrix_A[0][0] = 2.0 * intervals[0]
    matrix_A[0][1] = intervals[0]
    vector_rhs[0] = 3.0 * ((nodes_y[1] - nodes_y[0]) / intervals[0])

    matrix_A[num_intervals][num_intervals - 1] = intervals[-1]
    matrix_A[num_intervals][num_intervals] = 2.0 * intervals[-1]
    vector_rhs[num_intervals] = 3.0 * \
        ((nodes_y[-1] - nodes_y[-2]) / intervals[-1])

    # Прямой ход метода Гаусса
    for i in range(num_intervals + 1):
        # Нормализация текущей строки
        pivot = matrix_A[i][i]
        for j in range(i, num_intervals + 1):
            matrix_A[i][j] /= pivot
        vector_rhs[i] /= pivot

        # Исключение переменной в последующих строках
        for k in range(i + 1, num_intervals + 1):
            factor = matrix_A[k][i]
            for j in range(i, num_intervals + 1):
                matrix_A[k][j] -= factor * matrix_A[i][j]
            vector_rhs[k] -= factor * vector_rhs[i]

    # Обратный ход метода Гаусса
    for i in range(num_intervals, -1, -1):
        coeff_c[i] = vector_rhs[i]
        for j in range(i + 1, num_intervals + 1):
            coeff_c[i] -= matrix_A[i][j] * coeff_c[j]

    # Вычисление коэффициентов b и d
    for i in range(num_intervals):
        coeff_b[i] = ((nodes_y[i + 1] - nodes_y[i]) / intervals[i] -
                      intervals[i] * (2.0 * coeff_c[i] + coeff_c[i + 1]) / 3.0)
        coeff_d[i] = (coeff_c[i + 1] - coeff_c[i]) / (3.0 * intervals[i])

    return coeff_a, coeff_b, coeff_c[:-1], coeff_d


def integrate_spline(nodes_x, coeff_a, coeff_b, coeff_c, coeff_d):
    integral = 0.0
    for i in range(len(nodes_x) - 1):
        h = nodes_x[i + 1] - nodes_x[i]
        # Интеграл от a + b*(x-x_i) + c*(x-x_i)^2 + d*(x-x_i)^3
        term_a = coeff_a[i] * h
        term_b = coeff_b[i] * h**2 / 2.0
        term_c = coeff_c[i] * h**3 / 3.0
        term_d = coeff_d[i] * h**4 / 4.0
        integral += term_a + term_b + term_c + term_d
    return integral


def f(x):
    return 4.0 / (1.0 + x**2)


def main():
    n_values = [8, 32, 128]
    for n in n_values:
        h = 1.0 / n
        nodes_x = [i * h for i in range(n + 1)]
        nodes_y = [f(x) for x in nodes_x]

        a, b, c, d = create_spline(nodes_x, nodes_y)

        approx_pi = integrate_spline(nodes_x, a, b, c, d)
        error = abs(approx_pi - math.pi)

        print(f"n = {n}, h = {h:.6f}")
        print(f"Приближение к π: {approx_pi:.12f}")
        print(f"Ошибка: {error:.12f}")
        print("-" * 50)


if __name__ == "__main__":
    main()
