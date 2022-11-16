frase = input('Digite uma frase: ').strip().lower()

print(f'A letra A aparece {frase.count("a")} na frase.')
print(f'A primeira letra A aparece na posição {frase.find("a")}')
print(f'A ultima letra A aparece na posição {frase.rfind("a")}')
