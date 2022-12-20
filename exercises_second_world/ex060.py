from math import factorial

n = int(input('Write a number: '))
print(f'Factorial of {n} is {factorial(n)}')

print('-=-' * 25)

c = n
f = 1
print(f'Factorial of {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f"{f}")
