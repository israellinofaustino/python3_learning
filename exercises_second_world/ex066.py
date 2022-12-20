sum = 0
count = 0

while True:
    n = int(input('Write a number (999 to stop): '))
    if n == 999:
        break
    sum += n
    count += 1
print('-=' * 20)
print(f'The quantity of numbers entered was {count}')
print(f'The total sum is: {sum}')
