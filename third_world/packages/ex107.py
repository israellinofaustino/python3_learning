from time import sleep
import calculus


calculus.line()
price = int(input("WRITE A PRICE => £").strip())
calculus.line()
sleep(1)
print(f"Half of £{price} is £{calculus.divdouble(price)}")
calculus.line()
sleep(1)
print(f"The double of £{price} is £{calculus.double(price)}")
calculus.line()
sleep(1)
print(f"Increasing by 10% we get => £{calculus.increase_value(price, tax=10)}")
calculus.line()
