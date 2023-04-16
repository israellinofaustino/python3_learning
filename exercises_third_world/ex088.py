from random import randint
from time import sleep

list_ = list()
games = list()
print('-'*20)
print(" GAMES FROM MEGA-SENA")
print('-'*20)

quant = int(input("How many games do you want to draw? => "))
total = 1
while total <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in list_:
            list_.append(num)
            count += 1
        if count >= 6:
            break
    list_.sort()
    games.append(list_[:])
    list_.clear()
    total += 1

print()
print(f"-=-=-= DRAWING {quant} GAMES -=-=-=")
for i, l in enumerate(games):
    print(f"Game {i+1}: {l}")
    sleep(1)
