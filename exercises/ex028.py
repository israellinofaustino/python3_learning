import random
import time

print('--=--' * 12)
print('Vou pensar em um numero entre 0 e 5 tente adivinhar......')
print('--=--' * 12)
n_aleatorio = random.randint(0, 5)

n = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if n_aleatorio == n:
    print(
        f'Ebaaaa você acertou, eu pensei no numero {n_aleatorio} e você digitou {n}')
else:
    print(f'Você perdeu, eu pensei no numero {n_aleatorio} e não no {n}')
