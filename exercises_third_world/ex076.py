produtos = ('Lapis', 1.75,
            'Borracha', 2.10,
            'Caderno', 25.60,
            'Estojo', 5.90,
            'Transferidor', 4.50,
            'Compasso', 10.20,
            'Mochila', 97.99,
            'Canetas', 15.40,
            'Livros', 249.99)

print('-=' * 20)
print(f'{"PRICE LIST":^40}')
print('-=' * 20)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-=' * 20)
