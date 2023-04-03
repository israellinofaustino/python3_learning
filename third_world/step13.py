test = []
guys = []

test.append("Israel")
test.append(25)

guys.append(test[:])

test[0] = "Israel Faustino"
test[1] = 28
guys.append(test[:])

print(guys)
print(guys[0][1])
print(guys[1][0])

people = [["Israel Lino Faustino", 25], ["Samara Delean Costa Fraga", 26],
          ["Alex Lima", 27], ["Maria da Silva", 28], ["João Pedro", 29]]

print(people[0])
print(people[0][0])
print(people[0][1])

print(people[1])
print(people[1][0])
print(people[1][1])

print(people[2])
print(people[2][0])
print(people[2][1])

print(people[3])
print(people[3][0])
print(people[3][1])

print(people[4])
print(people[4][0])
print(people[4][1])

print("-=" * 22)
for p in people:
    print(f"{p[0]} is {p[1]} years old.")
print("-=" * 22)

temp = []
ppl = []

for c in range(0, 3):
    temp.append(input("Name: "))
    temp.append(int(input("Age: ")))
    ppl.append(temp[:])
    temp.clear()
print(ppl)

totyoung = totolder = 0

for p in ppl:
    if p[1] >= 21:
        print(f"{p[0]} is older than others.")
        totolder += 1
    else:
        print(f"{p[0]}, is young than others")
        totyoung += 1
print(f"We have {totolder} older people and {totyoung} young people")
