from time import sleep
import calculus


calculus.line()
price = float(input("WRITE A PRICE => £").strip())
calculus.line()
sleep(1)
print(f"Half of pound sterling {calculus.format_currency(price)} is {calculus.format_currency(calculus.divdouble(price), currency='$')} in dollars.")
calculus.line()
sleep(1)
print(f"The double of {calculus.format_currency(price)} is {calculus.format_currency(calculus.double(price))}")
calculus.line()
sleep(1)
print(f"Increasing by 10% we get => {calculus.format_currency(calculus.increase_value(price, tax=10))}")
calculus.line()
