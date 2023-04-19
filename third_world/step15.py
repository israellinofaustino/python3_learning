def title(text):
    print('-' * 25)
    print(f'{text:^25}')
    print('-' * 25)


def sum_(* values):
    s = 0
    for n in values:
        s += n
    print(f'Adding the values {values} we have the total of {s}')


def line():
    print('-' * 25)


def counter(*num):
    for n in num:
        print(n, end=', ')
    print('END!')
    print(f'The size of your tuple is: {len(num)}')


def double(lst):
    position = 0
    while position < len(lst):
        lst[position] *= 2
        position += 1


title('London, UK')
title('United Kingdon')
title('Englando, UK')

line()
sum_(2, 4, 1, 3)
line()
sum_(10, 20, 5.5, 5.5)
line()
sum_(1.5, 3.5)
line()

counter(1, 2, 3, 4, 5)
counter(0, 1, 2)
counter(9, 8, 7)
line()

list_ = [2, 3, 4, 1, 0, 5]
double(list_)
print(list_)
line()
