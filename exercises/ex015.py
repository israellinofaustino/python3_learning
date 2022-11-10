days_rent = float(input('How many days did you rent the car? '))
km_traveled = float(input('How many km were driven while you had the car? '))

price_per_day = float(60)
price_per_km = float(0.15)

rent_price = days_rent * price_per_day
price_km_traveled = km_traveled * price_per_km
total = rent_price + price_km_traveled

print(f'The total payable is: R${total :.2f}')
