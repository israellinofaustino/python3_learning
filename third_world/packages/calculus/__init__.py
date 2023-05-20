def line():
    """
    -> Creates a separator line used in the terminal (CMD).
    """
    print("-" * 35)


def factorial(n = 1):
    """
    -> Calculates the factorial of a number.
        n: receives the number to be calculated, default value is 1.
        return: the factorial value of the number passed to the parameter {n}.
    """
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def double(n=0, form=False):
    """
    -> Double a number x2.
         n: receives the number to be calculated, default value is 0.
         form: receives the value False by default, if it receives True it shows the value formatted with the currency symbol and decimal places.
         return: returns the value multiplied by 2.
    """
    answer = n * 2
    return answer if form is False else format_currency(answer) 


def triple(n=0, form=False):
    """
    -> Triple an amount x3.
         n: receives the number to be calculated, default value is 0.
         form: receives the value False by default, if it receives True it shows the value formatted with the currency symbol and decimal places.
         return: returns the value multiplied by 3.
    """
    answer = n * 3
    return answer if form is False else format_currency(answer)


def divdouble(n=0, form=False):
    """
    -> Calculates the division of a value by 2.
         n: receives the number to be calculated, default value is 0.
         form: receives the value False by default, if it receives True it shows the value formatted with the currency symbol and decimal places.
         return: returns the value divided by 3.
    """
    answer = n / 2
    return answer if form is False else format_currency(answer)


def increase_value(price=0, tax=0, form=False):
    """
    -> Calculates the increase of a value in percentage.
         price: value of some item.
         tax: percentage value to be added.
         form: receives the value False by default, if it receives True it shows the value formatted with the currency symbol and decimal places.
         return: returns the value with the added percentage.
    """
    answer = price + (price * tax / 100)
    return answer if form is False else format_currency(answer)


def decrease_value(price=0, tax=0, form=False):
    """
    -> Calculates the decrease of a value in percentage.
         price: value of some item.
         tax: percentage value to be decrease.
         form: receives the value False by default, if it receives True it shows the value formatted with the currency symbol and decimal places.
         return: returns the value with the decrease percentage.
    """
    answer = price-(price*tax/100)
    return answer if form is False else format_currency(answer)


def format_currency(price=0, currency='£'):
    """
    -> Format the string to display a more presentable value with decimal places and currency symbol.
        price: value of some item.
        currency: currency symbol, by default it receives the pound sterling symbol.
        return: returns the formatted and more presentable value for the user.
    """
    answer = f"{currency}{price:.2f}".replace('.', ',')
    return answer


def resume(price=0, taxupper=10, taxlower=5):
    line()
    print("AMOUNT SUMMARY".center(35))
    line()
    print(f"Price analyzed => \t{format_currency(price)}")
    print(f"Double the price => \t{double(price, True)}")
    print(f"Half-price => \t\t{divdouble(price, True)}")
    print(f"{taxupper}% raise => \t\t{increase_value(price, taxupper, True)}")
    print(f"{taxlower}% off => \t\t{decrease_value(price, taxlower, True)}")
    line()

