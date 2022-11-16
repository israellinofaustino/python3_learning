house_value = float(input('How much is the house? R$'))
salary = float(input('Write your salary. R$'))
years_to_pay = int(input('In how many years do you want to pay? '))

monthly_parcels = house_value / (years_to_pay * 12)
minimum = salary * 30 / 100

print('-=-' * 25)
print(f'To pay a house of {house_value :.2f} in {years_to_pay} years, the parcels will be {monthly_parcels :.2f}')
print('-=-' * 25)

if monthly_parcels >= minimum:
    print("SORRY, you don't have the value necessary to buy this house :( ")
else:
    print('YES, you can do this meal with us.')
print('Have a good one!')
