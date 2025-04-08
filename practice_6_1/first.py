import math


def f(t):
    return (2/math.sqrt(math.pi)) * math.e**(-t**2)


def calc(a, b):
    return (b - a) * f((a + b) / 2)


def main():
    x_nodes = [i / 10 for i in range(10)]
    print([math.erf(x) for x in x_nodes])
    summ = 0
    for i in range(len(x_nodes) - 1):
        summ += calc(x_nodes[i], x_nodes[i + 1])
        print(summ, end=", ")


if __name__ == "__main__":
    main()
