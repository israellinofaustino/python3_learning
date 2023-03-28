numbers = [[], []]

for n in range(1, 8):
    n = int(input(f"Write {n}° number: "))
    if n != 0:
        if n % 2 == 0:
            numbers[0].append(n)
        else:
            numbers[1].append(n)

print("-=" * 22)
print(f"The even values entered were => {sorted(numbers[0])}")
print(f"The odd values entered were => {sorted(numbers[1])}")
