from utils import jacobi, zendel, print_solution
from graphic import plot_residuals


def jacobi_solution(x0: list[float], A, b) -> list[float]:
    solution = jacobi(A, b, x0=x0)
    print_solution(solution[0], b, "Метод Зейделя")
    return solution


def zendel_solution(x0: list[float], A, b) -> list[float]:
    solution = zendel(A, b, x0=x0)
    print_solution(solution[0], b, "Метод Якоби")

    return solution


def main():
    A = [
        [12.14, 1.32, -0.78, -2.75],
        [-0.89, 16.75, 1.88, -1.55],
        [2.65, -1.27, -15.64, -0.64],
        [2.44, 1.52, 1.93, -11.43]
    ]

    b = [14.78, -12.14, -11.65, 4.26]
    x = [[0, 0, 0, 0], [1, 1, 1, 1], [-1, -1, -1, -1]]
    data = []
    for x0 in x:  # x0 - начальное приближение
        jacob_sol = jacobi_solution(x0, A, b)
        zen_sol = zendel_solution(x0, A, b)
        if all((i - j) < 1e-5 for i, j in list(zip(jacob_sol[0], zen_sol[0]))):
            print()
            print(f"Решения совпадают при {x0}".center(80))
            print()

        iterations_jacobi = [data["iteration"] for data in jacob_sol[1]]
        norm_residuals_jacobi = [data["residual"] for data in jacob_sol[1]]
        iterations_zendel = [data["iteration"] for data in zen_sol[1]]
        norm_residuals_zendel = [data["residual"] for data in zen_sol[1]]
        data.append([iterations_jacobi, norm_residuals_jacobi,
                    f"Метод Якоби при {x0}"])
        data.append([iterations_zendel, norm_residuals_zendel,
                    f"Метод Зейделя при {x0}"])
    plot_residuals(data)


if __name__ == "__main__":
    main()
