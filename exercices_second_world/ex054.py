from datetime import date


current_year = date.today().year
older = 0
younger = 0

for c in range(1, 8):
    year_birth = int(input(f'Write the {c}º year of birth: '))
    age = current_year - year_birth

    if age >= 18:
        older += 1
    elif age < 18:
        younger += 1

print('-=' * 30)
print(f'{older} people are older and {younger} people are younger')
print('-=' * 30)
