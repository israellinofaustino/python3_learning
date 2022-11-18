import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computer_choice = random.randint(0, 2)

print('''
[0] - Pedra
[1] - Papel
[2] - Tesoura
''')

your_choice = int(input('Write your choice: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO!')

print('-=' * 13)
print(f'Computador jogou {itens[computer_choice]}')
print(f'Jogador jogou {itens[your_choice]}')
print('-=' * 13)

if computer_choice == 0:
    if your_choice == 0:
        print('EMPATE')
    elif your_choice == 1:
        print('JOGADOR VENCE')
    elif your_choice == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada INVALIDA')
elif computer_choice == 1:
    if your_choice == 0:
        print('COMPUTADOR VENCE')
    elif your_choice == 1:
        print('EMPATE')
    elif your_choice == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada INVALIDA')
elif computer_choice == 2:
    if your_choice == 0:
        print('JOGADOR VENCE')
    elif your_choice == 1:
        print('COMPUTADOR VENCE')
    elif your_choice == 2:
        print('EMPATE')
    else:
        print('Jogada INVALIDA')
else:
    print('Tente novamente')
