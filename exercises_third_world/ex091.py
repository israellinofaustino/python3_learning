from random import randint
from operator import itemgetter
from time import sleep

gamers = {'gamer1': randint(1, 6),
          'gamer2': randint(1, 6),
          'gamer3': randint(1, 6),
          'gamer4': randint(1, 6)
          }

ranking = list()
print("-=-=-=-= Dice Game -=-=-=-=")
for k, v in gamers.items():
    print(f'{k} got => {v}')
    sleep(1)

ranking = sorted(gamers.items(), key=itemgetter(1), reverse=True)

print('-=' * 14)

for i, v in enumerate(ranking):
    print(f'{i+1}º place => {v[0]} with {v[1]}')
    sleep(1)
print("-=-=-=-=   END!   -=-=-=-=")
