import math

angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print(f'O seno de {angulo} é ==> {seno :.2f}')

cosseno = math.cos(math.radians(angulo))
print(f'O cosseno de {angulo} é ==> {cosseno :.2f}')

tangente = math.tan(math.radians(angulo))
print(f'A tangente de {angulo} é ==> {tangente :.2f}')
