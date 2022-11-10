a = int(input('Primeiro num: '))
b = int(input('Segundo num: '))
c = int(input('Terceiro num: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número é {maior} e o menor é {menor}')
