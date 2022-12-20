num = int(input('Write some number: '))
choices = int(input('Choice 1 to banary, 2 to octal or 3 to hexadecimal: '))

if choices == 1:
    print(bin(num)[2:])
elif choices == 2:
    print(oct(num)[2:])
elif choices == 3:
    print(hex(num)[2:])
else:
    print('You need choice a numbem 1, 2 or 3')
