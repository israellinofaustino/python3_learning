upper_18 = registered_mens = womans_under_20 = 0

while True:
    age = int(input('Write your age => ').strip())

    gener = ' '
    while gener not in 'MF':
        gener = input('Write your gener [M/F] => ').strip().upper()[0]

    contin = ' '
    while contin not in 'YN':
        contin = input('Do you want to continue? [Y/N] => ').strip().upper()[0]

    if age > 18:
        upper_18 += 1
    if gener == 'M':
        registered_mens += 1
    if age < 20 and gener == 'F':
        womans_under_20 += 1

    if contin == 'Y':
        continue
    else:
        break

print('-=' * 30)
print(f'{upper_18} people are over 18 years old.')
print('-=' * 30)
print(f'{registered_mens} men were registered.')
print('-=' * 30)
print(f'{womans_under_20} women are under 20 years old.')
print('-=' * 30)
