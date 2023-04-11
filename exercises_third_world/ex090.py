from time import sleep
people = dict()

people['name'] = str(input("Name => "))
people['average'] = float(input(f"{people['name']} average => "))

if people['average'] < 5:
    people['situation'] = 'Disapproved'

if people['average'] >= 5 and people['average'] <= 7:
    people['situation'] = 'Recuperation'
else:
    people['situation'] = 'Approved'

print('-=' * 20)
for k, v in people.items():
    print(f'{k} is equal {v}')
    sleep(1)
print('-=' * 20)
