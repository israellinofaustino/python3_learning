from datetime import date


born = int(input('Write your born year: '))
current_year = date.today().year
age = current_year - born

print(f'Your age is {age}')
if age <= 9:
    print('Classification: LITTLE')
elif age <= 14:
    print('Classification: CHILDREN')
elif age <= 19:
    print('Classification: JUNIOR')
elif age <= 25:
    print('Classification: SENIOR')
elif age > 25:
    print('Classification: MASTER')
