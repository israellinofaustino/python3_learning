velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade <= 80:
    print('Okay, tenha um bom dia!')
else:
    print(f'\nMultado em R${(velocidade - 80) * 7 :.2f}')
    print('Você execeu o limite permitido que é 80Km/h.')
