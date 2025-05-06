import matplotlib.pyplot as plt


def runge_kutta_system(functions, initial_conditions, alpha, t_start, t_end, h):
    t_values = []
    r_values = []
    f_values = []

    t = t_start
    r, f = initial_conditions

    t_values.append(t)
    r_values.append(r)
    f_values.append(f)

    while t < t_end:
        k1_r = h * functions[0](r, f, alpha)
        k1_f = h * functions[1](r, f, alpha)

        k2_r = h * functions[0](r + k1_r / 2, f + k1_f / 2, alpha)
        k2_f = h * functions[1](r + k1_r / 2, f + k1_f / 2, alpha)

        k3_r = h * functions[0](r + k2_r / 2, f + k2_f / 2, alpha)
        k3_f = h * functions[1](r + k2_r / 2, f + k2_f / 2, alpha)

        k4_r = h * functions[0](r + k3_r, f + k3_f, alpha)
        k4_f = h * functions[1](r + k3_r, f + k3_f, alpha)

        r += (k1_r + 2 * k2_r + 2 * k3_r + k4_r) / 6
        f += (k1_f + 2 * k2_f + 2 * k3_f + k4_f) / 6

        t += h

        t_values.append(t)
        r_values.append(r)
        f_values.append(f)

        if r < 0:
            r = 0
        if f < 0:
            f = 0

        if r == 0 and f == 0:
            break

    return t_values, r_values, f_values


def dr_dt(r, f, alpha):
    return 2 * r - alpha * r * f


def df_dt(r, f, alpha):
    return -f + alpha * r * f


alpha = 0.01
t_start = 0
t_end = 10
h = 0.01

initial_conditions_list = [
    (15, 22),  # Заданные в задаче условия
    (100, 100),  # Равные начальные популяции
    (200, 10),  # Много кроликов, мало лис
    (10, 200),  # Мало кроликов, много лис
    (300, 300),  # Большие равные популяции
    (3000, 3000),  # ОООООООООчень большие равные популяции
    (2, 2),  # Маленькие равные популяции
]

for i, (r0, f0) in enumerate(initial_conditions_list):
    plt.figure(figsize=(10, 6))

    t, r, f = runge_kutta_system([dr_dt, df_dt], (r0, f0), alpha, t_start, t_end, h)

    plt.plot(t, r, "b-", label=f"Кролики (начально: {r0})")
    plt.plot(t, f, "r--", label=f"Лисы (начально: {f0})")

    final_r = r[-1]
    final_f = f[-1]
    plt.title(f"Динамика популяций\n Конечные значения: r={round(final_r, 3)}, f={round(final_f, 3)}")
    plt.xlabel("Время")
    plt.ylabel("Численность")
    plt.legend()
    plt.grid()

    plt.show()

print("\nПоиск начальных условий, при которых вымирают лисы:")
test_conditions = [(10, 5), (20, 5), (50, 5), (100, 5)]
for r0, f0 in test_conditions:
    t, r, f = runge_kutta_system([dr_dt, df_dt], (r0, f0), alpha, t_start, t_end, h)
    print(f"r0={r0}, f0={f0}: конечные значения - r={round(r[-1], 3)}, f={round(f[-1], 3)}")

print("\nПоиск условий с r0 = f0, при которых вымирают оба вида:")
test_conditions = [(1, 1), (2, 2), (5, 5), (10, 10)]
for r0, f0 in test_conditions:
    t, r, f = runge_kutta_system([dr_dt, df_dt], (r0, f0), alpha, t_start, t_end, h)
    print(f"r0=f0={round(r0, 3)}: конечные значения - r={round(r[-1], 3)}, f={round(f[-1], 3)}")
