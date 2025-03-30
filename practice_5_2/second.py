from first import *

# Узловые точки
nodes_x = [2, 3, 5, 7]
nodes_y = [4, -2, 6, -3]


def main():
    coeff_a, coeff_b, coeff_c, coeff_d = create_spline(nodes_x, nodes_y)

    x_values = [i / 100.0 for i in range(200, 701)]
    spline_values = [evaluate_spline(x, nodes_x, coeff_a, coeff_b, coeff_c, coeff_d) for x in x_values]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, spline_values, label='Кубический сплайн', color='blue')
    plt.scatter(nodes_x, nodes_y, color='red', label='Узловые точки')  # Узлы
    plt.title('Кубический сплайн для заданной таблицы значений')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()

    table = PrettyTable()
    table.field_names = ["x", "Значение сплайна", "Правильное значение", "Отклонение"]

    for x, y in zip(nodes_x, nodes_y):
        spline_at_node = evaluate_spline(x, nodes_x, coeff_a, coeff_b, coeff_c, coeff_d)
        table.add_row([x, spline_at_node, y, spline_at_node - y])

    print(table)


if __name__ == '__main__':
    main()
