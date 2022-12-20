n1 = int(input('Write the first number: '))
n2 = int(input('Write the second number: '))
print('-=-' * 20)
if n1 > n2:
    print('The first number is larger.'.upper())
elif n2 > n1:
    print('The second number is larger.'.upper())
else:
    print('There is no greater value, both are equal.'.upper())
print('-=-' * 20)
