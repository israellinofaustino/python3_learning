sum = 0
count = 0

for c in range(1, 7):
    numbers = int(input(f'Write the {c}º number: '))
    if numbers % 2 == 0:
        sum += numbers
        count += 1
print(f'You entered {count} even numbers and the sum was {sum}')
