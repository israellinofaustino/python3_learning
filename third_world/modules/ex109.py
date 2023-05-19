from time import sleep
import calculus


calculus.line()
price = float(input("WRITE A PRICE => £").strip())
calculus.line()
sleep(1)

print(f"Half of pound sterling {calculus.format_currency(price)} is {calculus.divdouble(price, True)}.")

calculus.line()
sleep(1)

print(f"The double of {calculus.format_currency(price)} is {calculus.double(price, True)}")

calculus.line()
sleep(1)

print(f"Increasing by 10% we get => {calculus.increase_value(price, tax=10, form=True)}")

calculus.line()
sleep(1)

print(f"Reducing 13% we have => {calculus.decrease_value(price, tax=13, form=True)}")

calculus.line()
