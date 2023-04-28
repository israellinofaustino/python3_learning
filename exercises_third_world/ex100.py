from random import randint
from time import sleep


values = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
even = []


def line():
    print("-=" * 28)


def rand_num():
    print(f"Drawing {len(values)} values from the list:",end=" ")
    for n in values:
        print(n, end=" ", flush=True)
        sleep(0.5)
    print("DONE!", end="")
    print()


def sum_even_numbers():
    for number in values:
        if number % 2 == 0:
            even.append(number)
    print(f"Sum the even values of: {values}, we have {sum(even)}")
    

line()
rand_num()
line()
sum_even_numbers()
line()
