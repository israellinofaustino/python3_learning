import random

v = 0

while True:
    player = int(input('Write a number: '))
    comp = random.randint(0, 10)
    total = player + comp
    type = ' '
    while type not in 'EO':
        type = input('Even or Odd? [E/O] => ').strip().upper()[0]
    print(f'You played {player} and the computer {comp}. Total of {total} - ', end='')
    print('GAVE PAIR' if total % 2 == 0 else 'GAVE ODD')
    if type == 'E':
        if total % 2 == 0:
            print('YOU WIN!')
            v += 1
        else:
            print('You lost.')
            break
    elif type == 'O':
        if total % 2 == 1:
            print('YOU WIN!')
            v += 1
        else:
            print('You lost.')
            break
    print("Let's play again...")
print(f'GAME OVER!, You won {v} times.')
