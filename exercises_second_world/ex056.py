soma_idade = 0
media_idade = 0
nome_velho = ''
maior_idade_homem = 0
mulheres_menos_de_20 = 0

for p in range(1, 5):
    nome = input('Escreva seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    genero = input('Digite seu genero - [M/F]: ').strip().upper()

    soma_idade += idade

    if p == 1 and genero == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if genero == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if genero == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

media_idade = soma_idade / 4

print('-=' * 30)
print(f'The average age of the group is {media_idade}')
print(f"The older man's name is {nome_velho} and he is {maior_idade_homem} years old.")
print(f'{mulheres_menos_de_20} women are under 20 years old.')
print('-=' * 30)
