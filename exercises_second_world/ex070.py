tot1000 = total = count = lower = 0
name_product_lower = ''

while True:
    name_product = input('Write the name of product: ').strip().upper()
    value = float(input('How much? $ ').strip())
    count += 1
    total += value

    if value >= 1000:
        tot1000 += 1

    if count == 1 or value < lower:
        lower = value
        name_product_lower = name_product

    contin = ' '
    while contin not in 'YN':
        contin = input('Do you want to continue? [Y/N] => ').strip().upper()[0]

    if contin == 'Y':
        continue
    else:
        break

print('-=' * 10)
print(f'The total amount spent on this purchase is ${total :.2f}')
print('-=' * 10)
print(f'{tot1000} cost more than $1000')
print('-=' * 10)
print(f'The cheapest product was {name_product_lower} and cost ${lower :.2f}')
print('-=' * 10)
