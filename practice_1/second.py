from prettytable import PrettyTable


def phi(x, k):
    return 1 / (k * (k + x))


def new_phi(x, k):
    return 1 / k - 1 / (k + 1)


def compute_sum_with_error(x, phi_fanc):
    k = 1
    new_value = phi_fanc(x, k)
    result = 0
    while new_value > 0.5 * 10 ** -8:
        k += 1
        result += new_value
        new_value = phi_fanc(x, k)
    return result


def main():
    result_table = PrettyTable(["x", "φ(x)", "φ(x) - φ(1)"])
    for x in range(11):
        x /= 10
        phi_x = compute_sum_with_error(x, phi)
        phi_1 = compute_sum_with_error(x, new_phi)
        result_table.add_row([x, phi_x, phi_x - phi_1])
    print(result_table)


main()
