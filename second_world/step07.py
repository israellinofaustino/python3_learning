for i in range(0, 11, 2):
    print(i)
print('-----END-----')
# =========================================================================== #
for c in range(15, 0, -1):
    print(f'{c} - Israel!')
print('THE END')
# =========================================================================== #
for count in range(10, 21):
    print(f'{count} - The end is here')
# =========================================================================== #
number = int(input('Write a number: '))
for c in range(0, number+1):
    print(c)
print('END')
# =========================================================================== #
start_count = int(input('Write a number to start: '))
end_count = int(input('Write a number to stop/end: '))
sequence_count = int(input('Write a number to sequence of count: '))
for i in range(start_count, end_count+1, sequence_count):
    print(i)
print('END')
# =========================================================================== #
s = 0
for c in range(0, 4):
    n = int(input('Write a number: '))
    s = s + n
print(f'The sum of all values is {s}')
# =========================================================================== #
