distancia = float(input('Qual a distancia da viagem em Km? ==> '))

if distancia <= 200:
    passagem_cara = distancia * 0.50
    print(f'A passagem vai custar R${passagem_cara :.2f}')
else:
    passagem_barata = distancia * 0.45
    print(f'A passagem vai custar R${passagem_barata :.2f}')
print('Tenha uma ótima viagem!!!')
