from random import shuffle


n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segunto nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')

list = [n1, n2, n3, n4]
shuffle(list)
print(f'A ordem de apresentação será \n {list}')
