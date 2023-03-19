list_num = []

for numbers, positions in enumerate(range(0, 5)):
    list_num.append(int(input(f'Write a number in possition {positions}: ')))
print(f'The numbers entered were: {list_num}')

print('-='*25)

print(f'Highest value: {max(list_num)} in the positions => ', end='')
for i, v in enumerate(list_num):
    if v == max(list_num):
        print(f'{i}...', end='')

print()

print(f'Lower value: {min(list_num)} in the positions => ', end='')
for i, v in enumerate(list_num):
    if v == min(list_num):
        print(f'{i}...', end='')

print()
print('-='*25)
