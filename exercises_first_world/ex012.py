product = float(input('Write the product value R$'))

discount = product * 5/100
applying_discount = product - discount

print(f'The product that cost R${product} in the 5% promotion it will cost R${applying_discount :.2f}')
