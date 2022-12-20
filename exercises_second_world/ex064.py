n = 0
acumulador = 0
sum = 0
n = int(input('Write a number: '))
while n != 999:
    acumulador += 1
    sum += n
    n = int(input('Write a number: '))
print(f'Você digitou {acumulador} números e a soma entre eles foi {sum}')
