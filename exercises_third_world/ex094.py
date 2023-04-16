people = list()
person = dict()
media = list()
women = list()

while True:
    person['name'] = str(input("Write a name: "))
    person['age'] = int(input("Write your age: "))
    media.append(person['age'])

    person['gener'] = str(input("Your gener [M/F]: ")).strip().upper()[0]
    if person['gener'] == 'F':
        women.append(person['name'])

    while person['gener'] != 'M' and person['gener'] != 'F':
        print("ERROR! Write again, you need choice M or F.")
        person['gener'] = input("Your gener [M/F]: ").strip().upper()[0]

    people.append(person.copy())
    question = str(input("Do you want continue? [Y/N]: ")).strip().upper()[0]

    while question != 'Y' and question != 'N':
        print("ERROR! Please write just Y or N.")
        question = input("Do you want continue? [Y/N]: ").strip().upper()[0]

    if question == "N":
        break

m = sum(media)/len(people)

print('-=' * 30)
print(f"In all, we have {len(people)} people registered.")
print('-=' * 30)
print(f"The average age is {m:.2f} years.")
print('-=' * 30)
print(f"The registered women were {women}")
print('-=' * 30)
print("Lista de pessoas que estão acima da média.")

for i in people:
    if i['age'] > m:
        print(f"     {i['name']} => {i['gener']} => {i['age']}")
