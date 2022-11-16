salario = float(input('Qual o seu salario? R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario :.2f} agora passa a ganhar R${novo :.2f}')
