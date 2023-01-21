n1 = int(input('Write a number: '))
n2 = int(input('Write another number: '))
n3 = int(input('Write more one number: '))
n4 = int(input('Write the lest one: '))
list_n = (n1, n2, n3, n4)

print(f'You wrote the numbers: {list_n}')
if 3 in list_n:
    print(f'The value 3 appears in the {list_n.index(3)+1}° position')
else:
    print('The value 3 was not entered.')
print('The even digitizer values were: ', end='')
for n in list_n:
    if n % 2 == 0:
        print(n, end=' - ')
print('END')
