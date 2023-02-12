list_numbers = list()

while True:
    user_num = int(input('Write a value: '))
    if user_num not in list_numbers:
        list_numbers.append(user_num)
    else:
        print('Valor duplicado... Não vou adicionar.')

    contin = input('Do you want continue? [Y/N] => ').upper().strip()[0]
    if contin == 'N':
        break

list_numbers.sort()
print(list_numbers)
