import random


aluno1 = input('Digite o primeiro nome: ')
aluno2 = input('Digite o segunto nome: ')
aluno3 = input('Digite o terceiro nome: ')
aluno4 = input('Digite o quarto nome: ')

list = [aluno1, aluno2, aluno3, aluno4]

escolha = random.choice(list)

print(f'O aluno(a) sorteado(a) foi ==> {escolha}')
