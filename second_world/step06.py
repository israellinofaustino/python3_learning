name = input('Write a name: ')
print('-=-' * 10)

if name == 'Israel':
    print('You have a nice name.')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Your name is so popular.')
elif name in 'Ana Claudia Jessica Juliana':
    print('You have a nice female name!')
else:
    print('Your name is normal.')
print(f'Have a good day, {name}.')
