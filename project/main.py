import math
import matplotlib.pyplot as plt


def exact_solution(x, t):
    return math.exp(-t) * math.sin(x)


def bib_bob(a, b, c, d):
    n = len(d)

    for i in range(1, n):
        m = a[i - 1] / b[i - 1]
        b[i] = b[i] - m * c[i - 1]
        d[i] = d[i] - m * d[i - 1]

    x = [0.0 for _ in range(n)]
    x[-1] = d[-1] / b[-1]

    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x


def solve_heat_equation(T=1.0, L=math.pi / 2, N=20, M=100, scheme="explicit"):
    """
    T - конечное время
    L - длина области по x
    N - количество узлов по пространству
    M - количество узлов по времени
    scheme - 'explicit' (явная) или 'implicit' (неявная схема)
    """
    h = L / (N - 1)  # шаг по пространству
    tau = T / (M - 1)  # шаг по времени
    r = tau / (h ** 2)  # коэффициент устойчивости

    if scheme == "explicit" and r > 0.5:
        print(
            f"Внимание: коэффициент r = {r:.3f} > 0.5, явная схема может быть неустойчивой"
        )

    # Здеся инициализируем сетку решения
    u = [[0 for i in range(N)] for j in range(M)]
    x = [i * h for i in range(N)]  # пространственные узлы
    t = [j * tau for j in range(M)]  # временные узлы

    # Закидываем в матрицу начальные условия (t = 0)
    for i in range(N):
        u[0][i] = math.sin(x[i])

    # Закидываем в матрицу граничные условия
    for j in range(M):
        u[j][0] = 0.0  # u(0,t) = 0
        u[j][N - 1] = math.exp(-t[j])  # u(L,t) = e^(-t)

    # Численное решение
    if scheme == "explicit":
        # Явная схема
        for j in range(M - 1):
            for i in range(1, N - 1):
                u[j + 1][i] = u[j][i] + r * (u[j][i + 1] - 2 * u[j][i] + u[j][i - 1])
    else:
        # Неявная схема
        for j in range(M - 1):
            # Тута происходит формирование матрицы системы и правой части
            a = [-r for _ in range(N - 1)]  # Элементы под диагональю
            b = [1 + 2 * r for _ in range(N)]  # главная диагональ
            c = [-r for _ in range(N - 1)]  # верхняя диагональ
            d = [0.0 for _ in range(N)]

            # Граничные условия
            b[0] = 1.0
            c[0] = 0.0
            d[0] = 0.0  # u(0,t) = 0

            b[-1] = 1.0
            a[-1] = 0.0
            d[-1] = math.exp(-t[j + 1])  # u(L,t) = e^(-t)

            # Правая часть для внутренних узлов
            for i in range(1, N - 1):
                d[i] = u[j][i]

            u_new = bib_bob(a, b, c, d)

            for i in range(N):
                u[j + 1][i] = u_new[i]

    return x, t, u


def plot_results(x, t, u, T, scheme_name):
    plt.figure(figsize=(12, 6))

    # Выбираем несколько времён
    time_indices = [0, len(t) // 4, len(t) // 2, 3 * len(t) // 4, len(t) - 1]
    for idx in time_indices:
        plt.plot(x, u[idx], label=f"t = {t[idx]:.2f}")

    # Точное решение в конечный момент времени
    exact = [exact_solution(xi, T) for xi in x]
    plt.plot(x, exact, "k--", linewidth=2, label="Точное решение (t=T)")

    plt.title(f"Решение уравнения теплопроводности ({scheme_name} схема)")
    plt.xlabel("Координата x")
    plt.ylabel("Температура u(x,t)")
    plt.legend()
    plt.grid(True)
    plt.show()


def calculate_errors(u, x, t):
    """
    Вычисление максимальной абсолютной ошибки
    """
    max_error = 0.0
    for j in range(len(t)):
        for i in range(len(x)):
            error = abs(u[j][i] - exact_solution(x[i], t[j]))
            if error > max_error:
                max_error = error
    return max_error


def main():
    T = 1.0  # Конечное время
    L = math.pi / 2  # Длина области
    N = 15  # Число узлов по пространству
    M = 15000  # Число узлов по времени

    print("=== Решение уравнения теплопроводности ===")
    print(f"Параметры: T = {T}, N = {N}, M = {M}")

    print("\nРасчет по явной схеме...")
    x, t, u_explicit = solve_heat_equation(T, L, N, M, "explicit")
    plot_results(x, t, u_explicit, T, "Явная")
    error_explicit = calculate_errors(u_explicit, x, t)
    print(f"Максимальная ошибка: {error_explicit:.6f}")

    print("\nРасчет по неявной схеме...")
    x, t, u_implicit = solve_heat_equation(T, L, N, M, "implicit")
    plot_results(x, t, u_implicit, T, "Неявная")
    error_implicit = calculate_errors(u_implicit, x, t)
    print(f"Максимальная ошибка: {error_implicit:.6f}")

    print("\nСравнение ошибок:")
    print(f"Явная схема: {error_explicit:.6f}")
    print(f"Неявная схема: {error_implicit:.6f}")


if __name__ == "__main__":
    main()
