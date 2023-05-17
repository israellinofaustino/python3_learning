from modules import calculus


num = int(input("Write a number: "))
fact = calculus.factorial(num)
print(f"The factorial of {num} is {fact}")
print(f"O dobro de {num} is {calculus.double(num)}")
print(f"O triplo de {num} is {calculus.triple(num)}")
