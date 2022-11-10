from phonenumbers import can_be_internationally_dialled


numero_digitado = int(input('Digite um numero de 0 a 9999: '))

print(f'Analisando o numero {numero_digitado}')
u = numero_digitado // 1 % 10
d = numero_digitado // 10 % 10
c = numero_digitado // 100 % 10
m = numero_digitado // 1000 % 10

print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')
