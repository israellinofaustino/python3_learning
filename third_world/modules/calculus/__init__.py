def factorial(n = 1):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def double(n = 0):
    return n * 2


def triple(n = 0):
    return n * 3


def divdouble(n = 0):
    return n / 2


def increase_value(price = 0, tax = 0):
    answer = price + (price * tax / 100)
    return answer


def decrease_value(price = 0, tax = 0):
    answer = price - (price * tax / 100)
    return answer


def line():
    print("-=" * 20)


def format_currency(price = 0, currency = '£'):
    answer = f"{currency}{price:.2f}".replace('.', ',')
    return answer

