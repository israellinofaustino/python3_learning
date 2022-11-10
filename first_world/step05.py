name = input('What is your name? ==> ')

if name == 'Israel':
    print('Nice name!')
else:
    print("I don't know how say your name hahahaha!")
print(f'Good morning {name}!!!')


n1 = float(input('Write the first note: '))
n2 = float(input('Write the second note: '))
m = (n1 + n2) / 2

print(f'Your average was {m}')

if m >= 6:
    print('Your average was good, Congrats!!!')
else:
    print('Your average was bad, study more!!!')
