people = {'name': 'Israel',
          'age': '25',
          'gener': 'M',
          'phone': 7756510694,
          'email': 'israel@gmail.com'
          }

people['name'] = 'Israel Lino'
people['weight'] = 105.8

print(people.keys())
print(people.values())
print(people.items())
print(people.get('name'))
print(type(people))
# del people['gener']

print('-=' * 40)
print(f"{people['name']} is {people['age']} years old and his phone number is => {people['phone']}")
print('-=' * 40)

for k in people.keys():  # .values() or .itens()
    print(k)

print('-=' * 20)

for k, v in people.items():
    print(f'{k} = {v}')

print('-=' * 20)

brazil = []
state1 = {'uf': 'Rio de Janeiro', 'sigle': 'RJ'}
state2 = {'uf': 'São Paulo', 'sigle': 'SP'}
brazil.append(state1)
brazil.append(state2)
print(brazil[0]['uf'])
print(brazil[1]['sigle'])

print('-=' * 20)

state = dict()
brazil = list()
for c in range(0, 3):
    state['uf'] = str(input('State => '))
    state['sigle'] = str(input('Sigle of state => '))
    brazil.append(state.copy())
print(brazil)

for e in brazil:
    for k, v in e.items():
        print(f'The item {k} => {v} value.')
