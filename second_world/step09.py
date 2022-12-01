n = 1
even = 0
odd = 0

while n != 0:
    n = int(input('Write a number: '))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'You entered {even} even and {odd} odd numbers.')
