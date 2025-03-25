import matplotlib.pyplot as plt

from prettytable import PrettyTable


def f(x):
    return 1 / (1 + 25 * x ** 2)


def create_spline(nodes_x, nodes_y):
    num_intervals = len(nodes_x) - 1
    intervals = [nodes_x[i + 1] - nodes_x[i] for i in range(num_intervals)]

    # Создание коэффициентов
    coeff_a = nodes_y[:-1]
    coeff_b = [0] * num_intervals
    coeff_d = [0] * num_intervals
    coeff_c = [0] * (num_intervals + 1)

    matrix_A = [[0] * (num_intervals + 1) for _ in range(num_intervals + 1)]
    vector_rhs = [0] * (num_intervals + 1)

    for i in range(1, num_intervals):
        matrix_A[i][i - 1] = intervals[i - 1]
        matrix_A[i][i] = 2 * (intervals[i - 1] + intervals[i])
        matrix_A[i][i + 1] = intervals[i]
        vector_rhs[i] = 3 * ((nodes_y[i + 1] - nodes_y[i]) / intervals[i] -
                             (nodes_y[i] - nodes_y[i - 1]) / intervals[i - 1])

    # Граничные условия
    matrix_A[0][0] = 1
    matrix_A[num_intervals][num_intervals] = 1

    # Метод Гаусса
    for i in range(num_intervals + 1):
        for j in range(i + 1, num_intervals + 1):
            if matrix_A[j][i] != 0:
                ratio = matrix_A[j][i] / matrix_A[i][i]
                for k in range(i, num_intervals + 1):
                    matrix_A[j][k] -= ratio * matrix_A[i][k]
                vector_rhs[j] -= ratio * vector_rhs[i]

    for i in range(num_intervals, -1, -1):
        sum_ax = 0
        for j in range(i + 1, num_intervals + 1):
            sum_ax += matrix_A[i][j] * coeff_c[j]
        coeff_c[i] = (vector_rhs[i] - sum_ax) / matrix_A[i][i]

    for i in range(num_intervals):
        coeff_b[i] = (nodes_y[i + 1] - nodes_y[i]) / intervals[i] - \
            intervals[i] * (2 * coeff_c[i] + coeff_c[i + 1]) / 3
        coeff_d[i] = (coeff_c[i + 1] - coeff_c[i]) / (3 * intervals[i])

    return coeff_a, coeff_b, coeff_c[:-1], coeff_d


def evaluate_spline(x_value, nodes_x, coeff_a, coeff_b, coeff_c, coeff_d):
    """
    Вычисляем сплайн в точке
    """
    for i in range(len(nodes_x) - 1):
        if nodes_x[i] <= x_value <= nodes_x[i + 1]:
            dx = x_value - nodes_x[i]
            return coeff_a[i] + coeff_b[i] * dx + coeff_c[i] * dx ** 2 + coeff_d[i] * dx ** 3
    return None


def main():
    x_range = [i / 100.0 for i in range(-100, 101)]
    function_values = [f(x) for x in x_range]

    num_nodes = [2, 8, 10, 12, 15]

    plt.figure(figsize=(10, 6))
    table = PrettyTable()
    table.field_names = ['n', 'Максимальное отклонение']

    plt.plot(x_range, function_values,
             label='Исходная функция f(x)', color='red')
    for n in num_nodes:
        # Создание равноотстоящих узлов
        nodes_x = [-1 + 2 * i / (n - 1) for i in range(n)]
        nodes_y = [f(x) for x in nodes_x]

        coeff_a, coeff_b, coeff_c, coeff_d = create_spline(nodes_x, nodes_y)

        spline_values = [evaluate_spline(
            x, nodes_x, coeff_a, coeff_b, coeff_c, coeff_d) for x in x_range]

        plt.plot(x_range, spline_values,
                 label=f'Кубический сплайн (n={n})', linestyle='--')
        plt.scatter(nodes_x, nodes_y, color='blue')  # Узлы

        deviations = [abs(function_values[i] - spline_values[i])
                      for i in range(len(function_values))]
        max_deviation = max(deviations)
        table.add_row([n, max_deviation])

    print(table)
    plt.title('Интерполяция функции f(x) с помощью кубического сплайна')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
