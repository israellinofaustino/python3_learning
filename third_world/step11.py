# tuples are IMMUTABLE

snacks = ('Hamburguer', 'Juice', 'Pizza', 'Pudim', 'Potato', 'Banana')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(c))
print(c.count(2))
print(c.index(5))

print(sorted(snacks))

for count in range(0, len(snacks)):
    print(f'I will eat {snacks[count]} in position {count}')

print('-=' * 10)

for position, food in enumerate(snacks):
    print(f'I will eat {food} in position {position}')

print('-=' * 10)

for food in snacks:
    print(f'I will eat {food}')

print('-=' * 10)

print('END')

print(snacks)
print(snacks[0])
print(snacks[1])
print(snacks[1:3])

print(snacks[2:])
print(snacks[-2])
print(snacks[-2:])
