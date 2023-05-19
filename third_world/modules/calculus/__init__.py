def factorial(n = 1):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def double(n=0, form=False):
    answer = n * 2
    return answer if form is False else format_currency(answer) 


def triple(n=0, form=False):
    answer = n * 3
    return answer if form is False else format_currency(answer)


def divdouble(n=0, form=False):
    answer = n / 2
    return answer if form is False else format_currency(answer)


def increase_value(price=0, tax=0, form=False):
    answer = price + (price * tax / 100)
    return answer if form is False else format_currency(answer)


def decrease_value(price=0, tax=0, form=False):
    answer = price-(price*tax/100)
    return answer if form is False else format_currency(answer)


def line():
    print("-=" * 20)


def format_currency(price=0, currency='£'):
    answer = f"{currency}{price:.2f}".replace('.', ',')
    return answer

