while True:
    n = int(input('Write a number to see a multiplication table: ').strip())
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} X {i} = {n * i}')
print('END')
