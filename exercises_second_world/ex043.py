weight = float(input('Write your current weight: '))
height = float(input('Write your current height: '))

BMI = weight / (height ** 2)

if BMI <= 18.5:
    print('Under weight')
elif 18.5 <= BMI < 25:
    print('Ideal weight')
elif 25 <= BMI < 30:
    print('Overweight')
elif 30 <= BMI < 40:
    print('Obesity')
elif BMI >= 40:
    print('Morbid obesity')
print(f'Your BMI is => {BMI :.1f}')
