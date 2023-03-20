temp = []
people = []
max_weight = min_weight = 0

while True:
    temp.append(input("Name: "))
    temp.append(float(input("Weight: ")))
    if len(people) == 0:
        max_weight = min_weight = temp[1]
    else:
        if temp[1] > max_weight:
            max_weight = temp[1]
        if temp[1] < min_weight:
            min_weight = temp[1]
    people.append(temp[:])
    temp.clear()

    still = input("Do you want continue? [Y/N] => ").strip().upper()[0]
    if still == "N":
        break

print("-=" * 25)

print(f"Altogether you have registered {len(people)} people.")

print("-=" * 25)

print(f"The highest weight was{max_weight}Kg. weight of ", end='')
for person in people:
    if person[1] == max_weight:
        print(f"[{person[0]}] ", end='')

print()

print(f"The lowest weight was {min_weight}Kg. weight of ", end='')
for person in people:
    if person[1] == min_weight:
        print(f"[{person[0]}] ", end='')
