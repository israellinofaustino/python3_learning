n = int(input('Write a number: '))

total = 0

for c in range(1, n + 1):
    if n % c == 0:  # Checking - Maybe is a PRIME number
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mThe number {n} was divisible {total} times.')

if total == 2:
    print('This is a PRIME number')
else:
    print('This is NOT a PRIMO number')
