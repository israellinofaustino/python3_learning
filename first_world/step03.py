#  import math  # will import all the functionality of the module
from math import sqrt, floor, ceil  # vai importar só a funcionalidade sqrt,
# imprtando dessa forma eu n preciso usar o math.sqrt é só digitar sqrt(num)


number = int(input('Write some number: '))

square_root = sqrt(number)

print(f'The square root of {number} is {square_root :.2f}')
print(f'The square root of {number} is {ceil(square_root) :.2f}')  # round up
print(f'The square root of {number} is {floor(square_root) :.2f}')  # round down

import emoji
print(emoji.emojize('Hello world :globe_showing_Americas:'))


import random
num = random.random()  # generates a random num between 0 and 1
numint = random.randint(1, 10)  # generates a num int from 1 to 10
print(num)
print(numint)
print(random.randint(1, 100))
