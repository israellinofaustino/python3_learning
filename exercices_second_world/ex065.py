n = 1
exit = ''
media = 0
storage = 0
numbers_written = 0
highest_n = 0
lower_n = 0

while exit != 'N':
    n = int(input('Write a number => '))
    exit = input('Do you want to continue? [Y/N] => ').upper().strip()[0]
    numbers_written += 1
    storage += n
    media = storage / numbers_written

    if numbers_written == 1:
        highest_n = lower_n = n
    else:
        if n > highest_n:
            highest_n = n
        if n < lower_n:
            lower_n = n

print(f'You entered {numbers_written} numbers and the average was {media}')
print(f'The highest value was {highest_n} and the lowest was {lower_n}')
print('END')
