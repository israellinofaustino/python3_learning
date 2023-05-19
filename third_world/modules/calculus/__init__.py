def factorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def double(n):
    return n * 2


def triple(n):
    return n * 3


def divdouble(n):
    return n / 2


def increase_value(price, tax):
    answer = price + (price * tax / 100)
    return answer


def decrease_value(price, tax):
    answer = price - (price * tax / 100)
    return answer


def line():
    print("-=" * 20)

