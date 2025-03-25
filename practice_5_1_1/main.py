def func(x):
    return 1 / (1 + 25 * x ** 2)


def get_y(func, x):
    return func(x)


x = [x / 100 for x in range(-100, 100)]

for i in x:
    print(f"f({i}) = {get_y(func, i)}")
