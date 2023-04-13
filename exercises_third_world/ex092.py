from datetime import date


person = dict()

person['nome'] = str(input("Write a name: "))
person['year_of_birth'] = int(input("Write your year of birth: "))
person['work_card'] = int(input("Write your work permit number (0 if you don't have): "))
person['year_of_hiring'] = int(input("Write your year of hiring (0 if you don't have): "))
person['salary'] = float(input("Write your salary (0 if you don't have) R$"))

person['age'] = date.today().year - person["year_of_birth"]
if person['work_card'] == 0:
    del person['year_of_birth']
    del person['salary']
    del person['year_of_hiring']
    print('-=' * 30)
    for k, v in person.items():
        print(f"  - {k} have the value {v}")
else:
    del person['year_of_birth']
    del person['year_of_hiring']
    print('-=' * 30)
    for k, v in person.items():
        print(f"  - {k} have the value {v}")
