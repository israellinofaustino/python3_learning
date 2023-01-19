num_extends = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'eleven', 'twelve ', 'thirteen',
               'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
               'nineteen', 'twenty')

while True:
    num = int(input('Write a number between 0 & 20 => '))
    if num <= 0 or num <= 20:
        print(f'You wrote number {num_extends[num]}.')
        print('Try again.', end=' ')

        ask = input('Du you want to try again? => ').strip().upper()[0]
        if ask == 'N':
            break
        else:
            continue
