nome_completo = input('Digite seu nome completo: ').strip()

nome_split = nome_completo.split()

print(f'Seu nome em maiusculas é {nome_completo.upper()}')
print(f'Seu nome em minusculas é {nome_completo.lower()}')
print(f'Seu nome tem {len(nome_completo) - nome_completo.count(" ")} letras')
print(f'Seu primeiro nome é {nome_split[0]} e tem {len(nome_split[0])} letras')
