from datetime import date

person = dict()

person['name'] = str(input("Write a name: "))
year_of_birth = int(input("Write your year of birth: "))
person['age'] = date.today().year - year_of_birth
person['work_card'] = int(input("Write your work permit number (0 if you don't have): "))
if person['work_card'] != 0:
    person['year_of_hiring'] = int(input("Write your year of hiring: "))
    person['salary'] = float(input("Write your salary R$"))
    person['retirement'] = person['age'] + ((person['year_of_hiring'] + 35) - date.today().year)
print('-=' * 30)
for k, v in person.items():
    print(f"  - {k} have the value {v}")
