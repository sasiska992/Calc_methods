import math

from prettytable import PrettyTable


def print_solution(solution: list[float], b: list[float], title: str):
    table = PrettyTable([f"x{i}" for i in range(len(b))])
    table.add_row(solution)
    print(title.center(80))
    print(table)


def is_diagonally_dominant(a) -> bool:
    for i in range(len(a)):
        summa = 0
        for j in range(len(a[i])):
            summa += abs(a[i][j]) if i != j else 0
        if abs(a[i][i]) <= summa:
            return False
    return True


def zendel(A, b, x0=None, error=1e-10, max_iterations=100):
    # x0 - начальное приближение
    if not is_diagonally_dominant(A):
        raise ValueError("У матрицы нет диагонального преобладания")

    graphic = []
    n = len(b)
    if x0 is None:  # Если x0 не задан, инициализируем его нулями
        x0 = [0.0] * n

    x = x0.copy()

    for k in range(max_iterations):
        x_old = x.copy()  # Сохраняем предыдущее значение x
        for i in range(n):
            sum1 = sum(A[i][j] * x[j]
                       for j in range(i))  # Сумма по предыдущим элементам
            sum2 = sum(A[i][j] * x_old[j]
                       # Сумма по следующим элементам
                       for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]  # Обновление x[i]

        ax = multiply_by_vector(A, x)
        idk = [a - b for a, b in zip(ax, b)]
        residual = norm([[math.pow(a, 2) for a in idk]])

        graphic.append({"residual": residual, "iteration": k})
        # Проверка на сходимость
        if max(abs(x[i] - x_old[i]) for i in range(n)) < error:
            return x, graphic

    # Выход из функции, если не удается достичь сходимости
    raise ValueError(
        "Метод Зейделя не сошелся за заданное количество итераций (ничего не вернулось)")


def jacobi(A, b, x0=None, error=1e-10, max_iterations=100):
    if not is_diagonally_dominant(A):
        raise ValueError("У матрицы нет диагонального преобладания")

    n = len(A)
    graphic = []
    if x0 is not None:
        x = x0
    else:
        x = [0] * n
    for iteration in range(max_iterations):
        x_new = [0] * n
        for i in range(n):
            summ = 0
            for j in range(n):
                if i != j:
                    summ += A[i][j] * x[j]
            x_new[i] = (b[i] - summ) / A[i][i]

        ax = multiply_by_vector(A, x_new)
        idk = [a - b for a, b in zip(ax, b)]
        residual = norm([[math.pow(a, 2) for a in idk]])
        graphic.append({"residual": residual, "iteration": iteration})
        # Проверка на сходимость
        if max(abs(x_new[i] - x[i]) for i in range(n)) < error:
            return x_new, graphic

        x = x_new

    # Выход из функции, если не удается достичь сходимости
    raise ValueError(
        "Метод Якоби не сошелся за заданное количество итераций (ничего не вернулось)")


def sub(m1, m2):
    result = []

    for i in range(len(m1)):
        result.append([m1[i][j] - m2[i][j] for j in range(len(m1[0]))])

    return result


def norm(matrix):
    sums = []
    cols = len(matrix[0])

    for i in range(cols):
        sums.append(sum([abs(matrix[j][i]) for j in range(len(matrix))]))

    return max(sums)


def multiply_by_vector(matrix, vector):
    result = []

    for i in range(len(matrix)):
        result.append(sum([matrix[i][j] * vector[j]
                      for j in range(len(matrix[0]))]))

    return result
