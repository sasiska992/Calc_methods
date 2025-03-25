import matplotlib.pyplot as plt


def plot_residuals(data):
    # Построение графика
    plt.figure(figsize=(10, 6))
    for iteration, norm, method in data:
        plt.plot(iteration, norm, label=method)

    plt.xlabel('Итерации')
    plt.ylabel('Норма невязки')
    plt.title('Зависимость нормы невязки от номера итерации')
    plt.legend()
    plt.grid()
    plt.yscale('log')
    plt.show()
