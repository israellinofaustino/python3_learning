# print(input.__doc__)
# help(input)


def counter(start, end, steps):
    """
    -> It counts and shows on the screen
     :param start: start of count
     :param end: end of count
     :param steps: counting steps
     :return: no return
    """
    c = start
    while c <= end:
        print(f"{c} ", end= "")
        c += steps
    print("END!")

help(counter)


def summ(a=0, b=0, c=0): #  I can use multiples params with *var
    """
    -> Sum 3 values with optional parameters
    """
    s = a + b + c
    print(f"The sum is: {s}")


help(summ)


def test(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A inside the function is => {a}")
    print(f"B inside the function is => {b}")
    print(f"C inside the function is => {c}")


a = 5
test(a)
print(f"A outside the function is => {a}")


def suum(a=0, b=0, c=0):
    s = a + b + c
    return s


quest1 = suum(2,3,5)
quest2 = suum(3,7,10)
quest3 = suum(8,8)

print(f"My calc is => {quest1} - {quest2} - {quest3}")

def even(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input("Write a number: "))
if even(n):
    print("It's Even.")
else:
    print("It's Odd.")
