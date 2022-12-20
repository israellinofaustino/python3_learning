gener = ''
while gener != 'M' and gener != 'F':
    gener = input('Write your gener [M / F]: ').strip().upper()[0]
    print('Write again, you need choice M or F.')
print(f"Great! You chose: {gener}")
