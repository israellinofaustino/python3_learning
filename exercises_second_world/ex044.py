product_cost = float(input('Write the product value R$'))
print('[1] - MONEY \n[2] - CARD \n[3] - 3X or more CREDT CARD \n[4] - 2X CREDT CARD')
form_of_payment = int(input('Which of these payment methods do you choose? => '))

discount_money = product_cost - (product_cost * 10 / 100)
card = product_cost - (product_cost * 5 / 100)
finance_three_times_card = product_cost + (product_cost * 20 / 100)

print('-=-' * 20)
if form_of_payment == 1:
    print(f'Your product will cost R${discount_money :.2f} with the 10% discount.')
elif form_of_payment == 2:
    print(f'Your product will cost R${card :.2f} with the 5% discount.')
elif form_of_payment == 3:
    amounts_installments = int(input('How many times do you want to finance? '))
    print('-=-' * 20)
    if amounts_installments >= 3:
        parcels = finance_three_times_card / amounts_installments
        print(f'Your purchase will be paid in {amounts_installments}X of R${parcels :.2f} WITH INTEREST')
        print(f'Your product will cost R${finance_three_times_card :.2f}')
    elif amounts_installments < 3 or form_of_payment == 4:
        parcels = product_cost / amounts_installments
        print(f'Your product will still cost R${product_cost :.2f} with installments of R${parcels}')
else:
    print("We don't have that option, please try again.")
print('-=-' * 20)
