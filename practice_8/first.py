import math


def erf(x):
    return math.erf(x)


def f(x):
    return erf(x) - 0.5


def df(x):
    return (2 / math.sqrt(math.pi)) * math.exp(-(x**2))


def newton_method(x0):
    x = x0
    for i in range(1000):
        fx = f(x)
        if abs(fx) < -(10**6):
            return x
        dfx = df(x)
        x = x - fx / dfx
    return x


solution = newton_method(0.5)
print("Решение уравнения erf(x) - 0.5 = 0:\nx =", solution)
