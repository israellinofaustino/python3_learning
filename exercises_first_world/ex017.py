from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hi = hypot(co, ca)
# hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai medir: {hi :.2f}')
