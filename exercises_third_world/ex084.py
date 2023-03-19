data = []
ppl = []
max_weight = 0

while True:
    data.append(input("Name: "))
    data.append(float(input("Weight: ")))
    ppl.append(data[:])
    data.clear()

    still = input("Do you want continue? [Y/N] => ").strip().upper()[0]
    if still == "N":
        break

print("-=" * 25)
print(f"Altogether you have registered {len(ppl)} people.")
# print(ppl)

