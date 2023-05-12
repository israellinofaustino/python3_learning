from math import factorial


def fact(n, show=False):
    """
    n = The number to be calculated.
    show = Optional, show the account in full or not.
    return = The factorial value of a number n.
    """
    listn = list()

    if show == True:
        for num in range(1, n+1):
            listn.append(num)
        print(listn, end=" => ")

    return factorial(n)


print(fact(15, True))
help(fact)
